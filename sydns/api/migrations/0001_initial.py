# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('master', models.CharField(blank=True, max_length=20, null=True)),
                ('last_check', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(max_length=6)),
                ('notified_serial', models.IntegerField(blank=True, null=True)),
                ('account', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'domains',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('ttl', models.IntegerField(blank=True, null=True)),
                ('prio', models.IntegerField(blank=True, null=True)),
                ('change_date', models.IntegerField(blank=True, null=True)),
                ('ordername', models.CharField(blank=True, max_length=255, null=True)),
                ('auth', models.IntegerField(blank=True, null=True)),
                ('disabled', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'records',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('level', models.IntegerField()),
                ('active', models.IntegerField()),
                ('perm_templ', models.IntegerField()),
                ('use_ldap', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_id', models.IntegerField()),
                ('owner', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('zone_templ_id', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'zones',
            },
        ),
    ]