# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('package', models.CharField(max_length=500, null=True, blank=True)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('version', models.CharField(max_length=50, null=True, blank=True)),
                ('size', models.CharField(max_length=50, null=True, blank=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('price', models.FloatField()),
                ('currency', models.CharField(max_length=50, null=True, blank=True)),
                ('evaluation', models.FloatField()),
                ('number_evaluations', models.BigIntegerField()),
                ('developer', models.CharField(max_length=500, null=True, blank=True)),
                ('iap', models.BooleanField()),
                ('training', models.BooleanField(default=False)),
                ('icon', models.CharField(max_length=500, null=True, blank=True)),
                ('market_url', models.CharField(max_length=500, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_update_at', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=500, null=True, blank=True)),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('application_id', models.ForeignKey(to='apps.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, null=True, blank=True)),
                ('label', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='description',
            name='language_id',
            field=models.ForeignKey(to='apps.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='family_id',
            field=models.ForeignKey(to='apps.Family'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='category_id',
            field=models.ForeignKey(to='apps.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='content_id',
            field=models.ForeignKey(to='apps.Content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='downloads_id',
            field=models.ForeignKey(to='apps.Downloads'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='permissions',
            field=models.ManyToManyField(to='apps.Permission'),
            preserve_default=True,
        ),
    ]
