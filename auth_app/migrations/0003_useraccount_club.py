# Generated by Django 4.0.4 on 2022-05-04 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
        ('auth_app', '0002_alter_useraccount_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='club.club'),
        ),
    ]
