# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150730_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_1',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
