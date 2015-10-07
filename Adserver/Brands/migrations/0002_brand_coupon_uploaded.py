# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brands', '0001_initial'),
        ('Coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='coupon_uploaded',
            field=models.ManyToManyField(related_name='_coupon_uploaded', to='Coupon.Coupon'),
        ),
    ]
