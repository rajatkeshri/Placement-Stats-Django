# Generated by Django 2.2.5 on 2020-06-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0002_auto_20200612_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydatabase',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
