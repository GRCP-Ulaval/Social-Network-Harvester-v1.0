# Generated by Django 2.1.1 on 2018-10-03 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='harvest_end',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 22, 40, 32, 827701)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='harvest_is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collection',
            name='harvest_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 22, 40, 46, 163804)),
            preserve_default=False,
        ),
    ]