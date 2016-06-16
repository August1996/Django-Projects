# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=280, verbose_name=b'\xe6\x96\x87\xe6\x9c\xac\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('image', models.ImageField(upload_to=b'/uploads', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('numb', models.IntegerField(default=0, verbose_name=b'\xe8\xa2\xab\xe8\x89\xbe\xe7\x89\xb9\xe6\xac\xa1\xe6\x95\xb0', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='expression',
            name='fromwhom',
            field=models.ForeignKey(related_name='fromwhom', verbose_name=b'\xe8\xa1\xa8\xe7\x99\xbd\xe8\x80\x85', to='items.Person'),
        ),
        migrations.AddField(
            model_name='expression',
            name='towhom',
            field=models.ForeignKey(related_name='towhom', verbose_name=b'\xe8\xa2\xab\xe8\xa1\xa8\xe7\x99\xbd\xe8\x80\x85', to='items.Person'),
        ),
    ]
