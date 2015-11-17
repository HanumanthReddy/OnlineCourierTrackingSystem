# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centeradmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='online_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ptype', models.CharField(max_length=128)),
                ('pweight', models.CharField(max_length=128)),
                ('pmail', models.CharField(max_length=128)),
                ('paddress', models.CharField(max_length=128)),
                ('pmobile', models.CharField(max_length=128)),
            ],
        ),
    ]
