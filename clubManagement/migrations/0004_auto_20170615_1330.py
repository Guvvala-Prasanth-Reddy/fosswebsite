# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('clubManagement', '0003_attendance_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responsibility',
            old_name='more_info',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='statusreport',
            old_name='img',
            new_name='image',
        ),
        migrations.AddField(
            model_name='statusreport',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project'),
        ),
    ]
