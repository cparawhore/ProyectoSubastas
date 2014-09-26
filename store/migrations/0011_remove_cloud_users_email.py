# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20140920_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloud_users',
            name='email',
        ),
    ]
