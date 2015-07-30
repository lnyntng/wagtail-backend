# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150729_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='category',
            field=models.CharField(default='LIU', max_length=12, choices=[('LIU', 'Laureate International Universities'), ('UNITEC', 'Universidad Tecnologica Centroamericana'), ('Walden', 'Walden University'), ('UVM', 'Universidad del Valle de Mexico')]),
        ),
    ]
