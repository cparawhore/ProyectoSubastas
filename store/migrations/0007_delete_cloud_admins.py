# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20140919_2339'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cloud_admins',
        ),
    ]
