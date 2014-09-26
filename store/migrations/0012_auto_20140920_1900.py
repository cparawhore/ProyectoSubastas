# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_cloud_users_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloud_users',
            name='id',
        ),
        migrations.AlterField(
            model_name='cloud_users',
            name='cloud_user',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
