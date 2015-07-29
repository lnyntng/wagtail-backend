# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150728_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', wagtail.wagtailcore.fields.StreamField([('section', wagtail.wagtailcore.blocks.RawHTMLBlock())])),
                ('category', models.CharField(default='signature', max_length=12, choices=[('signature', 'Signature'), ('discover', 'Discover')])),
            ],
        ),
    ]
