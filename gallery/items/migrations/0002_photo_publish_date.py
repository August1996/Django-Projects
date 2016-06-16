# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 10, 24, 56, 939847, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
