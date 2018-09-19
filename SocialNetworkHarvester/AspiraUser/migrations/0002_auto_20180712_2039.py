# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-07-12 20:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Youtube', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Facebook', '0001_initial'),
        ('AspiraUser', '0001_initial'),
        ('Twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebookPagesToHarvest',
            field=models.ManyToManyField(blank=True, related_name='harvested_by', to='Facebook.FBPage'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitterHashtagsToHarvest',
            field=models.ManyToManyField(blank=True, related_name='harvested_by', to='Twitter.HashtagHarvester'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitterUsersToHarvest',
            field=models.ManyToManyField(blank=True, related_name='harvested_by', to='Twitter.TWUser'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userProfile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ytChannelsToHarvest',
            field=models.ManyToManyField(blank=True, related_name='harvested_by', to='Youtube.YTChannel'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ytPlaylistsToHarvest',
            field=models.ManyToManyField(blank=True, related_name='harvested_by', to='Youtube.YTPlaylist'),
        ),
        migrations.AddField(
            model_name='tablerowsselection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tableRowsSelections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='selectionquery',
            name='selection_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queries', to='AspiraUser.TableRowsSelection'),
        ),
    ]