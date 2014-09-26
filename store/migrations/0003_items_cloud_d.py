# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20140919_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='items_cloud_d',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('it_nombre', models.CharField(max_length=200)),
                ('it_aspecto', models.CharField(max_length=200)),
                ('it_hero', models.CharField(max_length=200)),
                ('it_img', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
