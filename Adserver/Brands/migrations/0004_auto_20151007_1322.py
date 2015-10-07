# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coupon', '0002_remove_coupon_brand_uploaded'),
        ('Brands', '0003_auto_20151007_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='owner',
        ),
        migrations.AddField(
            model_name='brand',
            name='coupon_uploaded',
            field=models.ManyToManyField(related_name='_coupon_uploaded', to='Coupon.Coupon'),
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
