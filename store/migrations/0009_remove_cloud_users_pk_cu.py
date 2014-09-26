# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20140920_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloud_users',
            name='pk_cu',
        ),
    ]
