# Generated by Django 5.0.2 on 2024-02-16 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='math',
            name='first_number',
        ),
        migrations.RemoveField(
            model_name='math',
            name='second_number',
        ),
    ]