# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-02 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0007_auto_20191202_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='business/bizpic.jpg', upload_to='biz_pic/')),
                ('details', models.TextField(max_length=500)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbour.Hood')),
                ('mwenyeji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbour.User')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]