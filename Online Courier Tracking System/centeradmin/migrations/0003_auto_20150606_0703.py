# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centeradmin', '0002_online_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel_data',
            name='C_ID',
            field=models.ForeignKey(default=b'C0001', to='mainadmin.UserProfile'),
        ),
    ]
