# Generated by Django 3.2 on 2021-05-05 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', models.TextField(max_length=300, verbose_name='Content')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2021, 5, 5, 13, 24, 16, 772514))),
                ('url', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]