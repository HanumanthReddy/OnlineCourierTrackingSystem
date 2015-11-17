# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel_Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('P_ID', models.CharField(max_length=b'128')),
                ('P_Date', models.DateField(default=b'1990-11-05')),
                ('P_Source', models.CharField(max_length=b'128')),
                ('P_Destination', models.CharField(max_length=b'128')),
                ('P_A_Time', models.DateTimeField(auto_now_add=True)),
                ('P_D_Time', models.DateTimeField(auto_now_add=True)),
                ('P_Last', models.CharField(max_length=b'128')),
                ('P_Next', models.CharField(max_length=b'128')),
                ('P_Status', models.CharField(max_length=b'128', choices=[(b'In_Transit', b'In_Transit'), (b'Delivered', b'Delivered'), (b'Cancelled', b'Cancelled')])),
                ('C_ID', models.ForeignKey(to='mainadmin.UserProfile')),
            ],
        ),
    ]
