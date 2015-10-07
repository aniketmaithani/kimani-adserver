# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields
import uuid
from django.conf import settings
import django_extensions.db.fields
import uuid_upload_path.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, serialize=False, primary_key=True)),
                ('name_of_the_brand', models.CharField(help_text='Name of the brand', max_length=60)),
                ('email', models.EmailField(help_text='e-mail of the brand', max_length=255)),
                ('photo', versatileimagefield.fields.VersatileImageField(blank=True, upload_to=uuid_upload_path.storage.upload_to, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True, verbose_name='Address of the brand')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'ordering': ['-created'],
            },
        ),
    ]
