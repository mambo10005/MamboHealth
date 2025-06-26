from datetime import datetime
import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import ExtractYear, ExtractMonth
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .forms import HealthRecordForm
from .models import HealthRecord, HealthViewPreference, HealthFieldRange
from .utils import get_field_groups, get_field_labels, get_accordion_sections, get_disease_related_field_groups, model_to_dict_full

from django.core.serializers.json import DjangoJSONEncoder

from django.http import JsonResponse

import csv
from django.http import HttpResponse

from datetime import date
from decimal import Decimal

@login_required
def health_record_list(request):
    records = HealthRecord.objects.filter(user=request.user).order_by('-date_measured')

    years = records.annotate(year=ExtractYear('date_measured')).values_list('year', flat=True).distinct()
    months = records.annotate(month=ExtractMonth('date_measured')).values_list('month', flat=True).distinct()

    year = request.GET.get('year')
    month = request.GET.get('month')

    if year:
        records = records.filter(date_measured__year=year)
    if month:
        records = records.filter(date_measured__month=month)

    # Load or create user preferences
    pref, _ = HealthViewPreference.objects.get_or_create(user=request.user)

    if request.method == "POST":
        data = json.loads(request.body)
        pref.table_fields = data.get("table_fields", pref.table_fields)
        pref.chart_fields = data.get("chart_fields", pref.chart_fields)
        pref.save()
        return JsonResponse({"status": "ok"})

    # Selected fields for chart/table
    table_fields = pref.table_fields or ['systolic_bp', 'diastolic_bp', 'glucose', 'hb_a1c', 'cholesterol_total', 'cholesterol_ldl', 'cholesterol_hdl', 'cholesterol_vldl', 'triglyceride']
    chart_fields = pref.chart_fields or ['systolic_bp', 'diastolic_bp', 'glucose', 'hb_a1c', 'cholesterol_total', 'cholesterol_ldl', 'cholesterol_hdl', 'cholesterol_vldl', 'triglyceride']

    field_labels = get_field_labels()
    # Inside health_record_list view, before the render() call:
    field_groups = get_disease_related_field_groups()

    exam_fields = HealthFieldRange.objects.all()
    field_ranges = {f.field_name: (f.min_value, f.max_value, f.unit) for f in exam_fields}

    # ✅ Prepare records_json for Chart.js
    records_json = json.dumps([
        {
            **{f: getattr(r, f, None) for f in field_labels.keys()},
            'date': r.date_measured.strftime('%Y-%m-%d')
        } for r in records
    ], ensure_ascii=False, cls=DjangoJSONEncoder)

    return render(request, 'health_data/health_record_list.html', {
        'records': records,
        'years': sorted(set(years)),
        'months': sorted(set(months)),
        'selected_year': year,
        'selected_month': month,
        'field_labels': field_labels,
        'field_labels_json': json.dumps(field_labels, ensure_ascii=False),
        'records_json': records_json,
        'field_groups': field_groups,
        'table_fields': table_fields,
        'chart_fields': chart_fields,
        'field_ranges': field_ranges,
    })



@login_required
def health_record_detail(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk, user=request.user)

    return render(request, 'health_data/health_record_detail.html', {
        'record': record,
        'field_groups': get_disease_related_field_groups(),
        'accordion_sections': get_accordion_sections(),
        'field_labels': get_field_labels(),
    })


@login_required
def health_record_create(request):
    last_record = HealthRecord.objects.filter(user=request.user).order_by('-date_measured').first()
    form = None

    if request.method == 'POST':
        if "load_json" in request.POST:
            json_file = request.FILES.get("json_file")
            if json_file:
                try:
                    data = json.load(json_file)
                    if "date_measured" in data:
                        data["date_measured"] = datetime.strptime(data["date_measured"], "%Y-%m-%d").date()
                    form = HealthRecordForm(initial=data)
                    messages.info(request, "JSON 데이터가 성공적으로 불러와졌습니다. 아래에서 확인 후 저장해주세요.")
                except Exception as e:
                    messages.error(request, f"JSON 파일 처리 중 오류 발생: {e}")
            else:
                messages.warning(request, "JSON 파일을 업로드해주세요.")

        elif "copy_last" in request.POST and last_record:
            record_data = model_to_dict(last_record)
            record_data.pop("id", None)
            record_data.pop("user", None)
            form = HealthRecordForm(initial=record_data)
            messages.info(request, "최근 기록이 성공적으로 복사되었습니다. 확인 후 저장해주세요.")

        elif "submit" in request.POST:
            form = HealthRecordForm(request.POST)
            if form.is_valid():
                record = form.save(commit=False)
                record.user = request.user
                record.date_recorded = datetime.now()
                record.save()
                messages.success(request, "건강 기록이 성공적으로 저장되었습니다.")
                return redirect("health_data:health_record_list")
            else:
                messages.error(request, "저장 중 오류가 발생했습니다. 입력값을 확인해주세요.")

        else:
            form = HealthRecordForm(request.POST)

    if form is None:
        form = HealthRecordForm()

    return render(request, 'health_data/health_record_form.html', {
        'form': form,
        'has_last': last_record is not None,
        'field_groups': get_field_groups(),
        #'basic_info_fields': get_field_groups()["신체 측정"],
        'accordion_sections': [
            {
                'title': group_name,
                'id': f"group_{i}",
                'color': '#f8f9fa',
                'fields': fields
            }
            for i, (group_name, fields) in enumerate(get_disease_related_field_groups().items())
        ],
    })


@login_required
def health_record_update(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk, user=request.user)
    form = None

    if request.method == 'POST':
        if "load_json" in request.POST and request.FILES.get("json_file"):
            json_file = request.FILES["json_file"]
            try:
                data = json.load(json_file)
                if "date_measured" in data:
                    data["date_measured"] = datetime.strptime(data["date_measured"], "%Y-%m-%d").date()
                form = HealthRecordForm(data, instance=record)
                if form.is_valid():
                    messages.info(request, "JSON 데이터가 성공적으로 불러와졌습니다. 아래에서 확인 후 저장해주세요.")
                else:
                    messages.error(request, "JSON 형식은 올바르지만 일부 필드에 오류가 있습니다.")
            except Exception as e:
                messages.error(request, f"JSON 파일 처리 중 오류 발생: {e}")
        elif "submit" in request.POST:
            form = HealthRecordForm(request.POST, instance=record)
            if form.is_valid():
                updated_record = form.save(commit=False)
                updated_record.user = request.user
                updated_record.date_recorded = datetime.now()
                updated_record.save()
                messages.success(request, "건강 기록이 성공적으로 수정되었습니다.")
                return redirect("health_data:health_record_list")
        else:
            form = HealthRecordForm(request.POST, instance=record)

    if form is None:
        form = HealthRecordForm(instance=record)

    return render(request, 'health_data/health_record_form.html', {
        'form': form,
        'record': record,
        'field_groups': get_disease_related_field_groups(),
        #'basic_info_fields': get_field_groups()["신체 측정"],
        'accordion_sections': [
            {
                'title': group_name,
                'id': f"group_{i}",
                'color': '#f8f9fa',
                'fields': fields
            }
            for i, (group_name, fields) in enumerate(get_disease_related_field_groups().items())
        ],
    })


class HealthRecordDeleteView(DeleteView):
    model = HealthRecord
    template_name = 'health_data/health_record_confirm_delete.html'
    success_url = reverse_lazy('health_data:health_record_list')

    def get_queryset(self):
        return HealthRecord.objects.filter(user=self.request.user)
    

def serialize(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()  # e.g., '2025-06-23'
    elif isinstance(value, Decimal):
        return float(value)
    return value

def health_record_export_json(request, pk):
    record = HealthRecord.objects.get(pk=pk, user=request.user)
    data = model_to_dict(record)

    # Convert all fields to JSON-serializable types
    serializable_data = {k: serialize(v) for k, v in data.items()}

    response = HttpResponse(
        json.dumps(serializable_data, ensure_ascii=False, indent=2),
        content_type='application/json; charset=utf-8'
    )
    response['Content-Disposition'] = f'attachment; filename="health_record_{record.pk}.json"'
    return response

def health_record_export_csv(request, pk):
    record = HealthRecord.objects.get(pk=pk, user=request.user)
    fields = [f.name for f in HealthRecord._meta.fields if f.name != 'user']

    # Use BOM for Korean characters to work in Excel
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response.write('\ufeff')  # ⬅ UTF-8 BOM
    response['Content-Disposition'] = f'attachment; filename="health_record_{record.pk}.csv"'

    writer = csv.writer(response)
    writer.writerow(fields)
    writer.writerow([getattr(record, f) for f in fields])

    return response