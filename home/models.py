from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailadmin.edit_handlers import FieldPanel


EVENT_AUDIENCE_CHOICES = (
    ('signature', "Signature"),
    ('discover', "Discover"),
)


class HomePage(Page):
    body = RichTextField(blank=True)
    category = models.CharField(max_length=12, choices=EVENT_AUDIENCE_CHOICES, default='signature')

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('category', classname="full")
    ]