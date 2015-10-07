# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import uuid
import uuid_upload_path.storage
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Brands', '0003_auto_20151007_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('coupon_name', models.CharField(max_length=100, help_text='Name of the coupon. E.g FREE MASALA COFFEE')),
                ('photo_of_the_coupon', versatileimagefield.fields.VersatileImageField(blank=True, upload_to=uuid_upload_path.storage.upload_to, null=True)),
                ('coupon_code', models.CharField(max_length=100, help_text='Name of the coupon. E.g ERT101')),
                ('brand_uploaded', models.ManyToManyField(to='Brands.Brand', related_name='_uploaded_by')),
            ],
            options={
                'verbose_name_plural': 'coupons',
                'verbose_name': 'coupon',
                'ordering': ['-created'],
            },
        ),
    ]
