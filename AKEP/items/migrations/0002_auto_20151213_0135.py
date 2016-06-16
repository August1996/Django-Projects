# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expression',
            options={'ordering': ['-pub_time']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='expression',
            name='image',
        ),
    ]
