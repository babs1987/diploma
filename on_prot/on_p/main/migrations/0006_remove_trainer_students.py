# Generated by Django 4.1.4 on 2023-01-15 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_armwrestler_trainers_tournament'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='students',
        ),
    ]