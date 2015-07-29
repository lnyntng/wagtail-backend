# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_merge'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductPage',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RawHTMLBlock())]),
        ),
    ]
