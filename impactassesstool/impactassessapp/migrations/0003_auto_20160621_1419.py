# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0002_auto_20160620_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeneficiaryLevelIndicator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('organization', models.ForeignKey(to='impactassessapp.Organization')),
            ],
            options={
                'db_table': 'beneficiary_level_indicator',
            },
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'geography',
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_award', models.DateField(null=True, blank=True)),
                ('amount', models.IntegerField(null=True, blank=True)),
                ('amount_note', models.CharField(max_length=500, null=True, blank=True)),
                ('geography_note', models.CharField(max_length=200, null=True, blank=True)),
                ('cost_effectiveness', models.CharField(max_length=500, null=True)),
                ('beneficiary_level_indicator', models.CharField(max_length=500, null=True, blank=True)),
                ('organization_level_indicator', models.CharField(max_length=500, null=True, blank=True)),
                ('me_capacity_note', models.CharField(max_length=200, null=True, blank=True)),
                ('recommended_indicator', models.CharField(max_length=500, null=True, blank=True)),
                ('notes', models.CharField(max_length=500, null=True, blank=True)),
                ('geography', models.ForeignKey(to='impactassessapp.Geography', null=True)),
            ],
            options={
                'db_table': 'investment',
            },
        ),
        migrations.CreateModel(
            name='InvestmentCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'investment_category',
            },
        ),
        migrations.CreateModel(
            name='InvestmentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(to='impactassessapp.InvestmentCategory', null=True)),
            ],
            options={
                'db_table': 'investment_type',
            },
        ),
        migrations.CreateModel(
            name='IsIndicatorMet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'is_indicator_met',
            },
        ),
        migrations.CreateModel(
            name='MECapacity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'me_capacity',
            },
        ),
        migrations.CreateModel(
            name='OrganizationLevelIndicator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('organization', models.ForeignKey(to='impactassessapp.Organization')),
            ],
            options={
                'db_table': 'organization_level_indicator',
            },
        ),
        migrations.CreateModel(
            name='ReportDueDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'report_due_date',
            },
        ),
        migrations.CreateModel(
            name='ReportDueType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'report_due_type',
            },
        ),
        migrations.CreateModel(
            name='ReportStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'report_status',
            },
        ),
        migrations.CreateModel(
            name='ThematicArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'thematic_area',
            },
        ),
        migrations.AddField(
            model_name='reportduedate',
            name='report_due_type',
            field=models.ForeignKey(to='impactassessapp.ReportDueType', null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='investment_type',
            field=models.ManyToManyField(to='impactassessapp.InvestmentType'),
        ),
        migrations.AddField(
            model_name='investment',
            name='is_indicator_met',
            field=models.ForeignKey(to='impactassessapp.IsIndicatorMet', null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='me_capacity',
            field=models.ForeignKey(to='impactassessapp.MECapacity', null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='organization',
            field=models.ForeignKey(to='impactassessapp.Organization'),
        ),
        migrations.AddField(
            model_name='investment',
            name='report_due_date',
            field=models.ManyToManyField(to='impactassessapp.ReportDueDate'),
        ),
        migrations.AddField(
            model_name='investment',
            name='report_status',
            field=models.ForeignKey(to='impactassessapp.ReportStatus', null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='thematic_area',
            field=models.ForeignKey(to='impactassessapp.ThematicArea', null=True),
        ),
    ]
