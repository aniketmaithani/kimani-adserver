# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brands', '0002_auto_20151007_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='coupon_upload',
        ),
        migrations.AddField(
            model_name='coupon',
            name='owner',
            field=models.ManyToManyField(to='Brands.Brand'),
        ),
    ]
