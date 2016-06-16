# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import items.reclass


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Title')),
                ('desc', models.TextField(verbose_name=b'Description')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('intro', models.TextField(verbose_name=b'Introduction')),
                ('photo', items.reclass.photoAndthumbField(upload_to=b'uploads', verbose_name=b'Photo')),
                ('item', models.ForeignKey(verbose_name=b'Item', to='items.Item')),
            ],
        ),
    ]
