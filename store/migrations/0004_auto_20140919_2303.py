# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_items_cloud_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='bcc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pk_cu', models.IntegerField(max_length=11)),
                ('saldo', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cl_compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cl_user', models.IntegerField(max_length=11)),
                ('total', models.FloatField()),
                ('estado', models.IntegerField(max_length=11)),
                ('cant', models.IntegerField(max_length=11)),
                ('id_compra', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cl_compra_detalles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_item', models.CharField(max_length=9)),
                ('precio', models.FloatField()),
                ('cant', models.IntegerField(max_length=11)),
                ('id_compra', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cloud_admins',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cloud_user', models.CharField(max_length=50)),
                ('enc_pass', models.CharField(max_length=40)),
                ('pk_cu', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='hero_suge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuser', models.CharField(max_length=150)),
                ('suge', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='items_cloud_d',
            name='it_precio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items_cloud_d',
            name='it_stock',
            field=models.IntegerField(default=0, max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items_cloud_d',
            name='it_aspecto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='items_cloud_d',
            name='it_hero',
            field=models.CharField(max_length=100),
        ),
    ]
