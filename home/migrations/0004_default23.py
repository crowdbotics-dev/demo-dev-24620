# Generated by Django 2.2.26 on 2022-06-03 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220603_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default23',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]