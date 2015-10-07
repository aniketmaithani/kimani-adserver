# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import versatileimagefield.fields
import uuid
import uuid_upload_path.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4, editable=False)),
                ('coupon_name', models.CharField(max_length=100, help_text='Name of the coupon. E.g FREE MASALA COFFEE')),
                ('photo_of_the_coupon', versatileimagefield.fields.VersatileImageField(null=True, upload_to=uuid_upload_path.storage.upload_to, blank=True)),
                ('coupon_code', models.CharField(max_length=100, help_text='Name of the coupon. E.g ERT101')),
            ],
            options={
                'verbose_name': 'coupon',
                'ordering': ['-created'],
                'verbose_name_plural': 'coupons',
            },
        ),
    ]
