# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151122_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-click_num'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AddField(
            model_name='user',
            name='intro',
            field=models.TextField(default=datetime.datetime(2015, 11, 22, 4, 40, 26, 132593, tzinfo=utc), verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
            preserve_default=False,
        ),
    ]
