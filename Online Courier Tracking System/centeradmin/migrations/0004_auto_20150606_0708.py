# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centeradmin', '0003_auto_20150606_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel_data',
            name='P_Date',
            field=models.DateField(default=b'2015-06-06'),
        ),
    ]
