# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kaaster', '0006_auto_20160116_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagsinposts',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaaster.Post'),
        ),
        migrations.AlterField(
            model_name='tagsinposts',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaaster.Tag'),
        ),
    ]
