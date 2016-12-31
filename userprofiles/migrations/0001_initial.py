# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 16:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_client', models.BooleanField(default=True)),
                ('is_washr', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='static/media/images/avatars/', verbose_name='avatar')),
                ('first_name', models.CharField(blank=True, max_length=40, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='last name')),
                ('phone', models.CharField(blank=True, default='', max_length=20, verbose_name='phone number')),
                ('address', models.CharField(blank=True, default='', max_length=100, verbose_name='address')),
                ('city', models.CharField(blank=True, default='', max_length=100, verbose_name='city')),
                ('state', models.CharField(blank=True, default='', max_length=2, verbose_name='state')),
                ('country', models.CharField(blank=True, default='', max_length=100, verbose_name='country')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
