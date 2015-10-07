# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Third Party Stuff
from django.db import models
from uuid_upload_path import upload_to
from versatileimagefield.fields import VersatileImageField

# kimani-adserver Stuff
from Adserver.base.models import TimeStampedUUIDModel


class Coupon(TimeStampedUUIDModel):
    coupon_name = models.CharField(blank=False, null=False,
                                   max_length=100, help_text='Name of the coupon. E.g FREE MASALA COFFEE')
    photo_of_the_coupon = VersatileImageField(blank=True, null=True, upload_to=upload_to)
    coupon_code = models.CharField(
        blank=False, null=False, max_length=100, help_text='Name of the coupon. E.g ERT101')

    def __str__(self):
        return self.coupon_name

    class Meta:
        verbose_name = "coupon"
        verbose_name_plural = "coupons"
        ordering = ['-created']
