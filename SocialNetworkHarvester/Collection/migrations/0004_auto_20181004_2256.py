# Generated by Django 2.1.1 on 2018-10-04 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collection', '0003_collection_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]