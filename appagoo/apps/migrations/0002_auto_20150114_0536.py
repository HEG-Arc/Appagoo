# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='application',
            name='content_id',
        ),
        migrations.RemoveField(
            model_name='application',
            name='downloads_id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='family_id',
        ),
        migrations.RemoveField(
            model_name='description',
            name='application_id',
        ),
        migrations.RemoveField(
            model_name='description',
            name='language_id',
        ),
        migrations.AddField(
            model_name='application',
            name='category',
            field=models.ForeignKey(to='apps.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='content',
            field=models.ForeignKey(to='apps.Content', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='downloads',
            field=models.ForeignKey(to='apps.Downloads', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='family',
            field=models.ForeignKey(to='apps.Family', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='application',
            field=models.ForeignKey(to='apps.Application', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='language',
            field=models.ForeignKey(to='apps.Language', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='created',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='evaluation',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='iap',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='number_evaluations',
            field=models.BigIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='permissions',
            field=models.ManyToManyField(to='apps.Permission', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='price',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='updated',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='description',
            name='text',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
