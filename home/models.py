from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.serializers.json import DjangoJSONEncoder
import json

class HomePage(Page):
    hero_title = RichTextField(blank=True)
    hero_subtitle = RichTextField(blank=True)

    content = StreamField([
        ("info_section", blocks.RichTextBlock()),
        ("image_section", ImageChooserBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("content"),
    ]

    @method_decorator(login_required)
    def serve(self, request):
        from health_data.models import HealthRecord, HealthViewPreference
        from health_data.utils import get_field_labels

        records = HealthRecord.objects.filter(user=request.user).order_by('-date_measured')
        pref, _ = HealthViewPreference.objects.get_or_create(user=request.user)

        chart_fields = pref.chart_fields or [
            'systolic_bp', 'diastolic_bp', 'glucose', 'hb_a1c',
            'cholesterol_total', 'cholesterol_ldl', 'cholesterol_hdl',
            'cholesterol_vldl', 'triglyceride'
        ]

        field_labels = get_field_labels()

        records_json = json.dumps([
            {
                **{f: getattr(r, f, None) for f in field_labels.keys()},
                'date': r.date_measured.strftime('%Y-%m-%d')
            } for r in records
        ], ensure_ascii=False, cls=DjangoJSONEncoder)

        return render(request, "home/home_page.html", {
            'page': self,
            'health_records': records_json,
            'chart_fields': json.dumps(chart_fields),
            'field_labels': json.dumps(field_labels),
        })