# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_cloud_users_pk_cu'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloud_users',
            name='email',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cloud_users',
            name='verified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
