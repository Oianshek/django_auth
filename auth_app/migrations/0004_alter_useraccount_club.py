# Generated by Django 4.0.4 on 2022-05-04 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
        ('auth_app', '0003_useraccount_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.club'),
        ),
    ]