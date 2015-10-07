# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Third Party Stuff
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from uuid_upload_path import upload_to
from versatileimagefield.fields import VersatileImageField

# kimani-adserver Stuff
from Adserver.base.models import TimeStampedUUIDModel


@python_2_unicode_compatible
class Brand(TimeStampedUUIDModel):
    user = models.ForeignKey(User)
    name_of_the_brand = models.CharField(blank=False, null=False,
                                         max_length=60, help_text='Name of the brand')
    email = models.EmailField(blank=False, null=False,
                              max_length=255, help_text='e-mail of the brand')
    photo = VersatileImageField(blank=True, null=True, upload_to=upload_to)
    phone_number = models.CharField(blank=True, null=False, max_length=15)
    address = models.TextField(blank=True, null=False, verbose_name='Address of the brand')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"
        ordering = ['-created']
