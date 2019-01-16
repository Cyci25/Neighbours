# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhoodapp', '0002_auto_20181016_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_name', models.CharField(max_length=30)),
                ('occupants_count', models.IntegerField()),
                ('neighbourhood_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodapp.Location')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='neighbourhood_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodapp.Neighbourhood'),
        ),
    ]
