# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images-uploaded')),
                ('image_name', models.CharField(max_length=30)),
                ('image_caption', models.CharField(max_length=30)),
                ('image_likes', models.PositiveIntegerField()),
                ('image_comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='profile-pics')),
                ('bio', models.TextField()),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='image_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instapp.Profile'),
        ),
    ]