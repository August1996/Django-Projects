# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151122_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.URLField(max_length=48, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xbd\x91\xe7\xab\x99'),
        ),
    ]
