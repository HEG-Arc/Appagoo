# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20150114_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='last_update_at',
        ),
    ]
