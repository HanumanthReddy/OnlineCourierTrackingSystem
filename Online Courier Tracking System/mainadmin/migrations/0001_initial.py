# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('C_ID', models.CharField(max_length=128, unique=True, serialize=False, primary_key=True)),
                ('C_Name', models.CharField(unique=True, max_length=128)),
            ],
        ),
    ]
