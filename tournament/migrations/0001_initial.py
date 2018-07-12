# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Couple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(help_text='Positive for NS, negative for EW')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Board')),
                ('ew_couple', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ew_results', to='tournament.Couple')),
                ('ns_couple', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ns_results', to='tournament.Couple')),
            ],
            options={
                'ordering': ('board',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together=set([('board', 'ew_couple'), ('board', 'ns_couple')]),
        ),
    ]
