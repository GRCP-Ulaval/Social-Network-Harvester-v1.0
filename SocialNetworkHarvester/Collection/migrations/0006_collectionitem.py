# Generated by Django 2.1.1 on 2018-10-05 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook', '0004_auto_20181003_0159'),
        ('Youtube', '0002_auto_20180914_1818'),
        ('Twitter', '0002_auto_20180914_1818'),
        ('Collection', '0005_auto_20181005_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='Collection.Collection')),
                ('facebook_pages', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='collections_included_in', to='Facebook.FBPage')),
                ('twitter_hashtags', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='collections_included_in', to='Twitter.HashtagHarvester')),
                ('twitter_users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='collections_included_in', to='Twitter.TWUser')),
                ('youtube_channels', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='collections_included_in', to='Youtube.YTChannel')),
                ('youtube_playlists', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='collections_included_in', to='Youtube.YTPlaylist')),
            ],
        ),
    ]
