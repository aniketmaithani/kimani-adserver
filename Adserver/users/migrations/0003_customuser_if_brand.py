# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151007_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='if_brand',
            field=models.BooleanField(default=False, verbose_name='if_brand'),
        ),
    ]
