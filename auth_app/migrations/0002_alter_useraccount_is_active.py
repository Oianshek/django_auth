# Generated by Django 4.0.4 on 2022-05-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
