# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20140919_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='items_cloud_d',
            name='it_id',
            field=models.CharField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]
