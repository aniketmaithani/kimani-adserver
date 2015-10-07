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
            name='Brand',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4, editable=False)),
                ('name_of_the_brand', models.CharField(max_length=60, help_text='Name of the brand')),
                ('email', models.EmailField(max_length=255, help_text='e-mail of the brand')),
                ('photo', versatileimagefield.fields.VersatileImageField(null=True, upload_to=uuid_upload_path.storage.upload_to, blank=True)),
                ('phone_number', models.CharField(max_length=15, blank=True)),
                ('address', models.TextField(blank=True, verbose_name='Address of the brand')),
            ],
            options={
                'verbose_name': 'brand',
                'ordering': ['-created'],
                'verbose_name_plural': 'brands',
            },
        ),
    ]
