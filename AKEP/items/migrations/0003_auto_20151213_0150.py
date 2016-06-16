# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20151213_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expression',
            name='towhom',
            field=models.ForeignKey(verbose_name=b'\xe8\xa2\xab\xe8\xa1\xa8\xe7\x99\xbd\xe8\x80\x85', to='items.Person'),
        ),
    ]
