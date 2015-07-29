from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailcore import blocks

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel


EVENT_AUDIENCE_CHOICES = (
    ('signature', "Signature"),
    ('discover', "Discover"),
)


class HomePage(Page):
    body = StreamField([
        ('paragraph', blocks.RawHTMLBlock())
    ])
    category = models.CharField(max_length=12, choices=EVENT_AUDIENCE_CHOICES, default='signature')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        FieldPanel('category', classname="full")
    ]