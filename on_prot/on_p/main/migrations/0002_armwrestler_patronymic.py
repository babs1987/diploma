# Generated by Django 4.1.4 on 2023-01-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='armwrestler',
            name='patronymic',
            field=models.CharField(default='Бадал оглы', max_length=100),
        ),
    ]