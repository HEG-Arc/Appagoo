# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_remove_application_last_update_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='application',
            name='updated_at',
        ),
    ]
