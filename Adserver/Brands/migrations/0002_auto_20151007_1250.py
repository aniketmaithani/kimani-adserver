# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields
import django_extensions.db.fields
import uuid_upload_path.storage
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('id', models.UUIDField(editable=False, serialize=False, default=uuid.uuid4, primary_key=True)),
                ('coupon_name', models.CharField(help_text='Name of the coupon. E.g FREE MASALA COFFEE', max_length=100)),
                ('photo_of_the_coupon', versatileimagefield.fields.VersatileImageField(upload_to=uuid_upload_path.storage.upload_to, blank=True, null=True)),
                ('coupon_code', models.CharField(help_text='Name of the coupon. E.g ERT101', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='brand',
            name='coupon_upload',
            field=models.ManyToManyField(to='Brands.Coupon'),
        ),
    ]
