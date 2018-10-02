# Generated by Django 2.1.1 on 2018-10-02 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook', '0002_auto_20180914_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbreaction',
            name='from_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posted_reactions', to='Facebook.FBProfile'),
        ),
        migrations.AlterField(
            model_name='fbreaction',
            name='to_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='received_reactions', to='Facebook.FBComment'),
        ),
        migrations.AlterField(
            model_name='fbreaction',
            name='to_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='received_reactions', to='Facebook.FBPost'),
        ),
    ]
