# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0007_auto_20160621_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeneficiaryVsOrganizationalImpact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'beneficiary_vs_organizational_impact',
            },
        ),
        migrations.CreateModel(
            name='CostEffectiveness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'cost_effectiveness',
            },
        ),
        migrations.CreateModel(
            name='ExternalEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'external_evaluation',
            },
        ),
        migrations.CreateModel(
            name='IndexOfQuantitativeReporting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField(default=-1)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'index_of_quantitative_reporting',
            },
        ),
        migrations.CreateModel(
            name='IndexOfReflectiveReporting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField(default=-1)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'index_of_reflective_reporting',
            },
        ),
        migrations.RemoveField(
            model_name='investment',
            name='cost_effectiveness',
        ),
        migrations.AddField(
            model_name='investment',
            name='collaborations',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='lessons_learned',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='summary_of_data_reported',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='notes',
            field=models.TextField(null=True, verbose_name=b'Reporting comments and notes', blank=True),
        ),
        migrations.RemoveField(
            model_name='investment',
            name='thematic_area',
        ),
        migrations.AddField(
            model_name='investment',
            name='thematic_area',
            field=models.ManyToManyField(to='impactassessapp.ThematicArea'),
        ),
        migrations.AddField(
            model_name='investment',
            name='beneficiary_vs_organizational_impact',
            field=models.ForeignKey(to='impactassessapp.BeneficiaryVsOrganizationalImpact', null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='external_evaluation',
            field=models.ForeignKey(to='impactassessapp.ExternalEvaluation', null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='index_of_quantitative_reporting',
            field=models.ForeignKey(to='impactassessapp.IndexOfQuantitativeReporting', null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='index_of_reflective_reporting',
            field=models.ForeignKey(to='impactassessapp.IndexOfReflectiveReporting', null=True),
        ),
    ]
