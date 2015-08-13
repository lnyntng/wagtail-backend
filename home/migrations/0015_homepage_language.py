# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20150730_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='language',
            field=models.CharField(default='en', max_length=3, choices=[('en', 'English'), ('es', 'Spanish'), ('pt', 'Portuguese')]),
        ),
    ]
