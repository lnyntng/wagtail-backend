from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailcore import blocks

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks import StructBlock

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel


UNIVERSITY_CHOICES = (
    ('LIU', "Laureate International Universities"),
    ('UNITEC', "Universidad Tecnologica Centroamericana"),
    ('Walden', "Walden University"),
    ('UVM', "Universidad del Valle de Mexico"),
)

LANGUAGE_CHOICES = (
    ('en', "English"),
    ('es', "Spanish"),
    ('pt', "Portuguese")
)


class HomePage(Page):
    section_1 = models.TextField(null=False, blank=False)
    section_2 = models.TextField(null=False, blank=False)
    section_3 = models.TextField(null=False, blank=False)
    section_4 = models.TextField(null=False, blank=False)
    section_5 = models.TextField(null=False, blank=False)
    section_6 = models.TextField(null=False, blank=False)

    language = models.CharField(choices=LANGUAGE_CHOICES, default='en', max_length=3, null=False, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('section_1'),
        FieldPanel('section_2'),
        FieldPanel('section_3'),
        FieldPanel('section_4'),
        FieldPanel('section_5'),
        FieldPanel('section_6'),
        FieldPanel('language')
    ]


class Article(StructBlock):
    title = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=True)
    author = blocks.CharBlock(required=True)


class ArticlePage(Page):
    articles = StreamField([
        ('article', Article(required=True))
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('articles')
    ]