# Generated by Django 4.1.4 on 2023-01-06 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArmStyles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Armwrestler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sport_category', models.CharField(blank=True, max_length=4, null=True)),
                ('age', models.DateField(default=datetime.date(2005, 1, 1))),
                ('sex', models.CharField(default='m', max_length=3)),
                ('team', models.CharField(default='not', max_length=100)),
                ('weight_category', models.CharField(default='60', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=99)),
                ('lubovnica', models.CharField(default='333', max_length=30)),
                ('students', models.ManyToManyField(to='main.armwrestler')),
            ],
        ),
    ]