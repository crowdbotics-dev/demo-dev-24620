# Generated by Django 2.2.26 on 2022-06-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_xyz'),
    ]

    operations = [
        migrations.AddField(
            model_name='xyz',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='xyz',
            name='user',
            field=models.TextField(blank=True, null=True),
        ),
    ]
