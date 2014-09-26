# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_delete_cloud_admins'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloud_users',
            name='ste_acc_1_trd',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cloud_users',
            name='ste_acc_trd',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
