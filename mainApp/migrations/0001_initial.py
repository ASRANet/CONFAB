# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-10 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=40)),
                ('element_id', models.CharField(max_length=40)),
                ('order', models.IntegerField()),
                ('text', models.CharField(max_length=4000)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.InfoPage')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=40)),
                ('full_name', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue', models.CharField(blank=True, max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('abstract_deadline', models.DateField()),
                ('acceptance_deadline', models.DateField()),
                ('papers_deadline', models.DateField()),
                ('registration_deadline', models.DateField()),
                ('full_price_registration', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('student_price_registration', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('one_day_registration', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
    ]
