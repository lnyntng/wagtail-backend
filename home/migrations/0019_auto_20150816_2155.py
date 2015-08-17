# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_articlepage_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='articles',
            field=wagtail.wagtailcore.fields.StreamField([('article', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'author', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'picture', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True))], required=True))]),
        ),
    ]
