# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-14 11:14
from __future__ import unicode_literals

import SocialNetworkHarvester_v1p0.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SocialNetworkHarvester_v1p0', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_time', models.DateTimeField(default=SocialNetworkHarvester_v1p0.models.djangoNow)),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('image_time_label_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SocialNetworkHarvester_v1p0.Image_time_label')),
            ],
            options={
                'abstract': False,
            },
            bases=('SocialNetworkHarvester_v1p0.image_time_label',),
        ),
        migrations.CreateModel(
            name='SubscriberCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_time', models.DateTimeField(default=SocialNetworkHarvester_v1p0.models.djangoNow)),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_time', models.DateTimeField(default=SocialNetworkHarvester_v1p0.models.djangoNow)),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_time', models.DateTimeField(default=SocialNetworkHarvester_v1p0.models.djangoNow)),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YTChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_ident', models.BigIntegerField(null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('keywords', models.CharField(max_length=1000, null=True)),
                ('profileColor', models.CharField(max_length=16, null=True)),
                ('title', models.CharField(max_length=128, null=True)),
                ('userName', models.CharField(max_length=32, null=True)),
                ('publishedAt', models.DateTimeField(null=True)),
                ('hiddenSubscriberCount', models.BooleanField(default=False)),
                ('isLinked', models.BooleanField(default=False)),
                ('privacyStatus', models.CharField(max_length=32, null=True)),
                ('_deleted_at', models.DateTimeField(null=True)),
                ('_last_updated', models.DateTimeField(null=True)),
                ('_last_video_harvested', models.DateTimeField(null=True)),
                ('_error_on_update', models.BooleanField(default=False)),
                ('_error_on_harvest', models.BooleanField(default=False)),
                ('_update_frequency', models.IntegerField(default=1)),
                ('_harvest_frequency', models.IntegerField(default=1)),
                ('_has_reached_begining', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='YTComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_comments', to='Youtube.YTChannel')),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_threads', to='Youtube.YTChannel')),
                ('parent_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Youtube.YTComment')),
            ],
        ),
        migrations.CreateModel(
            name='YTPlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='Youtube.YTChannel')),
            ],
        ),
        migrations.CreateModel(
            name='YTPlaylistItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlistOrder', models.IntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Youtube.YTPlaylist')),
            ],
        ),
        migrations.CreateModel(
            name='YTVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Youtube.YTChannel')),
            ],
        ),
        migrations.AddField(
            model_name='ytplaylistitem',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='Youtube.YTVideo'),
        ),
        migrations.AddField(
            model_name='ytcomment',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_threads', to='Youtube.YTVideo'),
        ),
        migrations.AddField(
            model_name='viewcount',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_counts', to='Youtube.YTChannel'),
        ),
        migrations.AddField(
            model_name='videocount',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_counts', to='Youtube.YTChannel'),
        ),
        migrations.AddField(
            model_name='subscribercount',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_counts', to='Youtube.YTChannel'),
        ),
        migrations.AddField(
            model_name='contentimage',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_images', to='Youtube.YTChannel'),
        ),
        migrations.AddField(
            model_name='commentcount',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_counts', to='Youtube.YTChannel'),
        ),
    ]
