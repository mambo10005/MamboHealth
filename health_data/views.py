from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import HealthRecord
from .forms import HealthRecordForm
from datetime import datetime

from django.db.models.functions import ExtractYear, ExtractMonth

from django.views.generic import DeleteView
from django.urls import reverse_lazy

from django.forms.models import model_to_dict

@login_required
def health_record_list(request):
    records = HealthRecord.objects.all().order_by('-date_measured')

    # Extract available years and months
    years = records.annotate(year=ExtractYear('date_measured')).values_list('year', flat=True).distinct()
    months = records.annotate(month=ExtractMonth('date_measured')).values_list('month', flat=True).distinct()

    year = request.GET.get('year')
    month = request.GET.get('month')

    if year:
        records = records.filter(date_measured__year=year)
    if month:
        records = records.filter(date_measured__month=month)

    return render(request, 'health_data/health_record_list.html', {
        'records': records,
        'years': sorted(set(years)),
        'months': sorted(set(months)),
        'selected_year': year,
        'selected_month': month,
    })

@login_required
def health_record_detail(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk, user=request.user)

    # Same groupings as in the form view
    field_groups = {
        "신체 측정": ["date_measured", "height", "weight", "waist_line", "systolic_bp", "diastolic_bp"],
        "안과": ["ocular_tension_left", "ocular_tension_right", "fundus"],
        "청력": ["hearing"],
        "심전도": ["ekg"],
        "내시경": ["gastroscopy"],
        "영상 검사": ["abdominal_sono", "thyroid_sono", "male_pelvis_sono", "chest_xray_ct"],
        "당뇨 검사": ["glucose"],
        "간 기능": ["total_protein", "albumin", "globulin", "t_bilirubin", "d_bilirubin", "sgot_ast", "sgpt_alt",
                   "alk_phosphatase", "ggtp", "ag_ratio", "bilirubin_indirect", "hbsag", "hbsab"],
        "심근, 신장 및 대사": ["ldh", "bun", "creatinine", "egfr", "bc_ratio"],
        "지질 및 당": ["cholesterol_total", "cholesterol_ldl", "cholesterol_hdl", "triglyceride"],
        "감염 질환": ["rpr"],
        "혈액 검사": [
            "wbc", "segment", "band", "lymphocyte", "monocyte", "eosinophil", "basophil",
            "nucleated_rbc", "blast", "promyelocyte", "myelocyte", "metamyelocyte",
            "rbc", "hemoglobin", "hct", "mcv", "mch", "mchc", "rdw",
            "platelet", "pct", "mpv", "pdw"
        ],
        "통풍 및 류마티스": ["uric_acid", "ra_factor"],
        "암 표지자": ["afp", "cea", "psa", "ca199"],
        "갑상선": ["tsh", "free_t4"],
        "대변 검사": ["stool_occult_blood"],
        "소변 검사": [
            "urine_color", "urine_sg", "urine_ph", "urine_protein", "urine_glucose", "urine_ketone",
            "urine_bilirubin", "urine_nitrite", "urine_blood", "urine_urobilinogen", "urine_rbc",
            "urine_wbc", "urine_epithelial_cell", "urine_casts", "urine_bacteria", "urine_crystals", "urine_other"
        ],
        "체성분": [
            "body_water", "body_protein", "body_minerals", "body_fat_mass", "skeletal_muscle_mass",
            "percent_body_fat", "ecw_ratio"
        ],
        "부위별 근육량": ["right_arm", "left_arm", "trunk", "right_leg", "left_leg"]
    }

    field_labels = {
        "date_measured": "측정일",
        "height": "키 (cm)",
        "weight": "몸무게 (kg)",
        "waist_line": "허리둘레 (cm)",
        "systolic_bp": "수축기 혈압 (Systolic BP)",
        "diastolic_bp": "이완기 혈압 (Diastolic BP)",
        "cholesterol_total": "총 콜레스테롤 (Total Cholesterol)",
        "cholesterol_ldl": "LDL 콜레스테롤",
        "cholesterol_hdl": "HDL 콜레스테롤",
        "triglyceride": "중성지방 (Triglycerides)",
        "glucose": "공복 혈당 (Glucose)",
        "bmi": "체질량지수 (BMI)",
        "ocular_tension_left": "안압 (좌, mmHg)",
        "ocular_tension_right": "안압 (우, mmHg)",
        "fundus": "안저 소견 (Fundus)",
        "hearing": "청력 소견 (Hearing)",
        "ekg":"심전도 (EKG)",
        "gastroscopy":"위내시경 소견",
        "abdominal_sono":"상복부 초음파 소견",
        "thyroid_sono":"갑상선 초음파 소견",
        "male_pelvis_sono":"남성하복부 초음파 소견",
        "chest_xray_ct":"흉부 촬영",
        "total_protein":"총 단백질 (g/dL)",
        "albumin":"알부민 (Albumin: g/dL)",
        "globulin":"글로불린 (Globulin: g/dL)",
        "t_bilirubin":"총 빌리루빈 (T.Bilirubin: mg/dL)",
        "d_bilirubin":"직접 빌리루빈 (D.Bilirubin: mg/dL)",
        "sgot_ast":"혈청GOT (SGOT(AST): U/L)",
        "sgpt_alt":"혈청GPT (SGPT(ALT): U/L)",
        "alk_phosphatase":"알칼리포스파타제 (Alk.phosphatase: U/L)",
        "ggtp":"감마GTP: U/L",
        "ag_ratio":"A/G 비율 (A/G Ratio)",
        "bilirubin_indirect":"간접 빌리루빈 (mg/dL)",
        "hbsag":"B형 간염 항원 (HBsAg(ECLIA): COI)",
        "hbsab":"B형 간염 항체 (HBsAb(ECLIA): IU/L)",
        "ldh":"젖산탈수소효소 (LDH: U/L)",
        "bun":"요소질소 (BUN: mg/dL)",
        "creatinine":"크레아티닌 (Creatinine: mg/dL)",
        "egfr":"신사구체여과율 (e-GFR: mL/min/1.73㎡)",
        "bc_ratio":"BUN/Cr 비율 (B/C ratio)",
        "rpr":"매독검사 (RPR)",
        "wbc":"백혈구수 (WBC: ×10³/μL)",
        "segment":"중성구백분율 (Segment: %)",
        "band":"간상구백분율 (Band: %)",
        "lymphocyte":"임파구백분율 (Lymphocyte: %)",
        "monocyte":"단구백분율 (Monocyte: %)",
        "eosinophil": "호산구백분율 (Eosinophil: %)",
        "basophil":"염기구백분율 (Basophil: %)",
        "nucleated_rbc":"유핵적혈구수 (Nucleated RBC: /100WBCs)",
        "blast":"골수아구 (Blast: %)",
        "promyelocyte":"전골수구수 (Promyelocyte: %)",
        "myelocyte":"골수구수 (Myelocyte: %)",
        "metamyelocyte":"후골수구수 (Metamyelocyte: %)",
        "rbc":"적혈구수 (RBC: ×10⁶/μL)",
        "hemoglobin":"혈색소 (Hemoglobin: g/dL)",
        "hct":"혈구용적치 (HCT: %)",
        "mcv":"평균적혈구용적 (MCV: fL)",
        "mch":"적혈구혈색소 (MCH: pg)",
        "mchc":"적혈구혈색농도 (MCHC: %)",
        "rdw":"적혈구분포폭 (RDW: %)",
        "platelet":"혈소판수 (Platelet: ×10³/μL)",
        "pct":"혈소판크리트 (PCT: %)",
        "mpv":"평균혈소판용적 (MPV: fL)",
        "pdw":"혈소판분포폭 (PDW :%)",
        "uric_acid":"요산 (Uric acid: mg/dL)",
        "ra_factor":"류마티스 인자 (RA factor: IU/mL)",
        "afp":"알파태아단백 (AFP(ECLIA): ng/mL)",
        "cea":"태아성암항원 (CEA: ng/mL)",
        "psa":"전립선특이항원 (PSA: ng/mL)",
        "ca199":"암항원 (CA 19-9: U/mL)",
        "tsh":"갑상선자극호르몬: (TSH: µIU/mL)",
        "free_t4":"갑상선 Free T4 (ng/dL)",
        "stool_occult_blood":"분변 잠혈 반응",
        "urine_color":"소변 색",
        "urine_sg":"소변 비중",
        "urine_ph":"소변 산도 (pH)",
        "urine_protein":"소변 단백",
        "urine_glucose":"소변 포도당",
        "urine_ketone": "소변 케톤체 (Ketone Bodies)",
        "urine_bilirubin":"소변 빌리루빈 (Bilirubin)",
        "urine_nitrite":"소변 아질산염 (Nitrite)",
        "urine_blood":"요잠혈 (Blood)",
        "urine_urobilinogen":"소변 우로빌리노겐 (Urobilinogen)",
        "urine_rbc":"소변 적혈구 (개/HPF)",
        "urine_wbc":"소변 백혈구 (개/HPF)",
        "urine_epithelial_cell":"소변 상피세포 (개/HPF)",
        "urine_casts":"소변 원주",
        "urine_bacteria":"소변 세균",
        "urine_crystals":"소변 결정체",
        "urine_other":"소변 기타",
        "body_water":"체수분 (L)",
        "body_protein":"단백질량 (kg)",
        "body_minerals":"무기질량 (kg)",
        "body_fat_mass":"체지방량 (kg)",
        "skeletal_muscle_mass":"골격근량 (kg)",
        "percent_body_fat":"체지방률 (%)",
        "ecw_ratio":"세포외수분비율 (ECW/TBW)",
        "right_arm":"오른팔 근육량 (kg)",
        "left_arm":"왼팔 근육량 (kg)",
        "trunk":"몸통 근육량 (kg)",
        "right_leg":"오른다리 근육량 (kg)",
        "left_leg":"왼다리 근육량 (kg)",
    }

    accordion_sections = [
        {"title": "🔎 안과검사", "id": "eye", "color": "bg-danger-subtle", "fields": field_groups["안과"]},
        {"title": "🔎 청력검사", "id": "hearing", "color": "bg-danger-subtle", "fields": field_groups["청력"]},
        {"title": "🔎 심전도검사", "id": "ekg", "color": "bg-danger-subtle", "fields": field_groups["심전도"]},
        {"title": "🔎 내시경검사", "id": "endoscopy", "color": "bg-danger-subtle", "fields": field_groups["내시경"]},
        {"title": "🩸 영상검사", "id": "radiography", "color": "bg-danger-subtle", "fields": field_groups["영상 검사"]},
        {"title": "🍭 당뇨검사", "id": "diabetes", "color": "bg-light", "fields": field_groups["당뇨 검사"]},
        {"title": "🧪 간기능검사", "id": "liver", "color": "bg-warning-subtle", "fields": field_groups["간 기능"]},
        {"title": "🧪 심근, 신장 및 대사", "id": "kidney_metabolism", "color": "bg-warning-subtle", "fields": field_groups["심근, 신장 및 대사"]},
        {"title": "🧬 지질검사", "id": "lipid", "color": "bg-success-subtle", "fields": field_groups["지질 및 당"]},
        {"title": "🧬 감염성질환검사", "id": "infection", "color": "bg-success-subtle", "fields": field_groups["감염 질환"]},
        {"title": "🩸 혈액검사", "id": "blood", "color": "bg-danger-subtle", "fields": field_groups["혈액 검사"]},

        {"title": "🔎 통풍 및 류마티스", "id": "gout", "color": "bg-danger-subtle", "fields": field_groups["통풍 및 류마티스"]},
        {"title": "🧫 암표지자", "id": "cancer", "color": "bg-danger-subtle", "fields": field_groups["암 표지자"]},
        {"title": "🦋 갑상선검사", "id": "thyroid", "color": "bg-secondary-subtle", "fields": field_groups["갑상선"]},
        {"title": "💧 대변검사", "id": "stool", "color": "bg-info-subtle", "fields": field_groups["대변 검사"]},
        {"title": "💧 소변검사", "id": "urine", "color": "bg-info-subtle", "fields": field_groups["소변 검사"]},
        {"title": "💧 체성분", "id": "inbody", "color": "bg-info-subtle", "fields": field_groups["체성분"] + field_groups["부위별 근육량"]},
        #{"title": "🔎 기타 검사", "id": "others", "color": "bg-light", "fields": field_groups["통풍 및 류마티스"] + field_groups["기타"] if "기타" in field_groups else []},
    ]

    return render(request, 'health_data/health_record_detail.html', {
        'record': record,
        'field_groups': field_groups,
        'accordion_sections': accordion_sections,
        'field_labels': field_labels,
    })



@login_required
def health_record_create(request):
    last_record = HealthRecord.objects.filter(user=request.user).order_by('-date_measured').first()

    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            health_record = form.save(commit=False)
            health_record.user = request.user
            health_record.date_recorded = datetime.now()
            health_record.save()
            form.save_m2m()
            return redirect('health_data:health_record_list')
        else:
            print("Form is invalid:", form.errors)

    elif request.GET.get("copy_last") and last_record:
        record_data = model_to_dict(last_record)
        record_data.pop("id", None)
        record_data.pop("user", None)
        form = HealthRecordForm(initial=record_data)

    else:
        form = HealthRecordForm()

    field_groups = {
        "신체 측정": ["date_measured", "height", "weight", "waist_line", "systolic_bp", "diastolic_bp"],
        "안과": ["ocular_tension_left", "ocular_tension_right", "fundus"],
        "청력": ["hearing"],
        "심전도": ["ekg"],
        "내시경": ["gastroscopy"],
        "영상 검사": ["abdominal_sono", "thyroid_sono", "male_pelvis_sono", "chest_xray_ct"],
        "당뇨 검사": ["glucose"],
        "간 기능": ["total_protein", "albumin", "globulin", "t_bilirubin", "d_bilirubin", "sgot_ast", "sgpt_alt",
                   "alk_phosphatase", "ggtp", "ag_ratio", "bilirubin_indirect", "hbsag", "hbsab"],
        "신장 및 대사": ["ldh", "bun", "creatinine", "egfr", "bc_ratio"],
        "지질 및 당": ["cholesterol_total", "cholesterol_ldl", "cholesterol_hdl", "triglyceride"],
        "감염 질환": ["rpr"],
        "혈액 검사": [
            "wbc", "segment", "band", "lymphocyte", "monocyte", "eosinophil", "basophil",
            "nucleated_rbc", "blast", "promyelocyte", "myelocyte", "metamyelocyte",
            "rbc", "hemoglobin", "hct", "mcv", "mch", "mchc", "rdw",
            "platelet", "pct", "mpv", "pdw"
        ],
        "통풍 및 류마티스": ["uric_acid", "ra_factor"],
        "암 표지자": ["afp", "cea", "psa", "ca199"],
        "갑상선": ["tsh", "free_t4"],
        "대변 검사": ["stool_occult_blood"],
        "소변 검사": [
            "urine_color", "urine_sg", "urine_ph", "urine_protein", "urine_glucose", "urine_ketone",
            "urine_bilirubin", "urine_nitrite", "urine_blood", "urine_urobilinogen", "urine_rbc",
            "urine_wbc", "urine_epithelial_cell", "urine_casts", "urine_bacteria", "urine_crystals", "urine_other"
        ],
        "체성분": [
            "body_water", "body_protein", "body_minerals", "body_fat_mass", "skeletal_muscle_mass",
            "percent_body_fat", "ecw_ratio"
        ],
        "부위별 근육량": ["right_arm", "left_arm", "trunk", "right_leg", "left_leg"]
    }

    accordion_sections = [
        {"title": "🔎 안과검사", "id": "eye", "color": "bg-danger-subtle", "fields": field_groups["안과"]},
        {"title": "🔎 청력검사", "id": "hearing", "color": "bg-danger-subtle", "fields": field_groups["청력"]},
        {"title": "🔎 심전도검사", "id": "ekg", "color": "bg-danger-subtle", "fields": field_groups["심전도"]},
        {"title": "🔎 내시경검사", "id": "endoscopy", "color": "bg-danger-subtle", "fields": field_groups["내시경"]},
        {"title": "🩸 영상검사", "id": "radiography", "color": "bg-danger-subtle", "fields": field_groups["영상 검사"]},
        {"title": "🍭 당뇨검사", "id": "diabetes", "color": "bg-light", "fields": field_groups["당뇨 검사"]},
        {"title": "🧪 간기능검사", "id": "liver", "color": "bg-warning-subtle", "fields": field_groups["간 기능"]},
        {"title": "🧪 심근, 신장 및 대사", "id": "kidney_metabolism", "color": "bg-warning-subtle", "fields": field_groups["신장 및 대사"]},
        {"title": "🧬 지질검사", "id": "lipid", "color": "bg-success-subtle", "fields": field_groups["지질 및 당"]},
        {"title": "🧬 감염성질환검사", "id": "infection", "color": "bg-success-subtle", "fields": field_groups["감염 질환"]},
        {"title": "🩸 혈액검사", "id": "blood", "color": "bg-danger-subtle", "fields": field_groups["혈액 검사"]},

        {"title": "🔎 통풍 및 류마티스", "id": "gout", "color": "bg-danger-subtle", "fields": field_groups["통풍 및 류마티스"]},
        {"title": "🧫 암표지자", "id": "cancer", "color": "bg-danger-subtle", "fields": field_groups["암 표지자"]},
        {"title": "🦋 갑상선검사", "id": "thyroid", "color": "bg-secondary-subtle", "fields": field_groups["갑상선"]},
        {"title": "💧 대변검사", "id": "stool", "color": "bg-info-subtle", "fields": field_groups["대변 검사"]},
        {"title": "💧 소변검사", "id": "urine", "color": "bg-info-subtle", "fields": field_groups["소변 검사"]},
        {"title": "💧 체성분", "id": "inbody", "color": "bg-info-subtle", "fields": field_groups["체성분"] + field_groups["부위별 근육량"]},
        #{"title": "🔎 기타 검사", "id": "others", "color": "bg-light", "fields": field_groups["통풍 및 류마티스"] + field_groups["기타"] if "기타" in field_groups else []},
    ]

    return render(request, 'health_data/health_record_form.html', {
        'form': form,
        "has_last": last_record is not None,
        'field_groups': field_groups,
        'basic_info_fields': field_groups["신체 측정"],
        'accordion_sections': accordion_sections,
    })


@login_required
def health_record_update(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk, user=request.user)
    if request.method == 'POST':
        form = HealthRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('health_data:health_record_detail', pk=pk)
    else:
        form = HealthRecordForm(instance=record)

    field_groups = {
        "신체 측정": ["date_measured", "height", "weight", "waist_line", "systolic_bp", "diastolic_bp"],
        "안과": ["ocular_tension_left", "ocular_tension_right", "fundus"],
        "청력": ["hearing"],
        "심전도": ["ekg"],
        "내시경": ["gastroscopy"],
        "영상 검사": ["abdominal_sono", "thyroid_sono", "male_pelvis_sono", "chest_xray_ct"],
        "당뇨 검사": ["glucose"],
        "간 기능": ["total_protein", "albumin", "globulin", "t_bilirubin", "d_bilirubin", "sgot_ast", "sgpt_alt",
                   "alk_phosphatase", "ggtp", "ag_ratio", "bilirubin_indirect", "hbsag", "hbsab"],
        "신장 및 대사": ["ldh", "bun", "creatinine", "egfr", "bc_ratio"],
        "지질 및 당": ["cholesterol_total", "cholesterol_ldl", "cholesterol_hdl", "triglyceride"],
        "감염 질환": ["rpr"],
        "혈액 검사": [
            "wbc", "segment", "band", "lymphocyte", "monocyte", "eosinophil", "basophil",
            "nucleated_rbc", "blast", "promyelocyte", "myelocyte", "metamyelocyte",
            "rbc", "hemoglobin", "hct", "mcv", "mch", "mchc", "rdw",
            "platelet", "pct", "mpv", "pdw"
        ],
        "통풍 및 류마티스": ["uric_acid", "ra_factor"],
        "암 표지자": ["afp", "cea", "psa", "ca199"],
        "갑상선": ["tsh", "free_t4"],
        "대변 검사": ["stool_occult_blood"],
        "소변 검사": [
            "urine_color", "urine_sg", "urine_ph", "urine_protein", "urine_glucose", "urine_ketone",
            "urine_bilirubin", "urine_nitrite", "urine_blood", "urine_urobilinogen", "urine_rbc",
            "urine_wbc", "urine_epithelial_cell", "urine_casts", "urine_bacteria", "urine_crystals", "urine_other"
        ],
        "체성분": [
            "body_water", "body_protein", "body_minerals", "body_fat_mass", "skeletal_muscle_mass",
            "percent_body_fat", "ecw_ratio"
        ],
        "부위별 근육량": ["right_arm", "left_arm", "trunk", "right_leg", "left_leg"]
    }

    accordion_sections = [
        {"title": "🔎 안과검사", "id": "eye", "color": "bg-danger-subtle", "fields": field_groups["안과"]},
        {"title": "🔎 청력검사", "id": "hearing", "color": "bg-danger-subtle", "fields": field_groups["청력"]},
        {"title": "🔎 심전도검사", "id": "ekg", "color": "bg-danger-subtle", "fields": field_groups["심전도"]},
        {"title": "🔎 내시경검사", "id": "endoscopy", "color": "bg-danger-subtle", "fields": field_groups["내시경"]},
        {"title": "🩸 영상검사", "id": "radiography", "color": "bg-danger-subtle", "fields": field_groups["영상 검사"]},
        {"title": "🍭 당뇨검사", "id": "diabetes", "color": "bg-light", "fields": field_groups["당뇨 검사"]},
        {"title": "🧪 간기능검사", "id": "liver", "color": "bg-warning-subtle", "fields": field_groups["간 기능"]},
        {"title": "🧪 심근, 신장 및 대사", "id": "kidney_metabolism", "color": "bg-warning-subtle", "fields": field_groups["신장 및 대사"]},
        {"title": "🧬 지질검사", "id": "lipid", "color": "bg-success-subtle", "fields": field_groups["지질 및 당"]},
        {"title": "🧬 감염성질환검사", "id": "infection", "color": "bg-success-subtle", "fields": field_groups["감염 질환"]},
        {"title": "🩸 혈액검사", "id": "blood", "color": "bg-danger-subtle", "fields": field_groups["혈액 검사"]},

        {"title": "🔎 통풍 및 류마티스", "id": "gout", "color": "bg-danger-subtle", "fields": field_groups["통풍 및 류마티스"]},
        {"title": "🧫 암표지자", "id": "cancer", "color": "bg-danger-subtle", "fields": field_groups["암 표지자"]},
        {"title": "🦋 갑상선검사", "id": "thyroid", "color": "bg-secondary-subtle", "fields": field_groups["갑상선"]},
        {"title": "💧 대변검사", "id": "stool", "color": "bg-info-subtle", "fields": field_groups["대변 검사"]},
        {"title": "💧 소변검사", "id": "urine", "color": "bg-info-subtle", "fields": field_groups["소변 검사"]},
        {"title": "💧 체성분", "id": "inbody", "color": "bg-info-subtle", "fields": field_groups["체성분"] + field_groups["부위별 근육량"]},
        #{"title": "🔎 기타 검사", "id": "others", "color": "bg-light", "fields": field_groups["통풍 및 류마티스"] + field_groups["기타"] if "기타" in field_groups else []},
    ]

    return render(request, 'health_data/health_record_form.html', {
        'form': form,
        'record': record,
        'field_groups': field_groups,
        'basic_info_fields': field_groups["신체 측정"],
        'accordion_sections': accordion_sections,
    })


class HealthRecordDeleteView(DeleteView):
    model = HealthRecord
    template_name = 'health_data/health_record_confirm_delete.html'
    success_url = reverse_lazy('health_data:health_record_list')

    def get_queryset(self):
        # Ensure only the user's own records can be deleted
        return HealthRecord.objects.filter(user=self.request.user)