# Generated by Django 4.0.4 on 2022-05-04 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='slug',
        ),
    ]