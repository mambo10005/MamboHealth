from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

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
