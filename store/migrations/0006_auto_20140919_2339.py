# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_items_cloud_d_it_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloud_users',
            old_name='cloud_users',
            new_name='cloud_user',
        ),
        migrations.AddField(
            model_name='cloud_users',
            name='pk_cu',
            field=models.IntegerField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]
