# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20150814_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='university',
            field=models.CharField(default='LIU', max_length=10, choices=[('LIU', 'Laureate International Universities'), ('UNITEC', 'Universidad Tecnologica Centroamericana'), ('Walden', 'Walden University'), ('UVM', 'Universidad del Valle de Mexico')]),
        ),
    ]
