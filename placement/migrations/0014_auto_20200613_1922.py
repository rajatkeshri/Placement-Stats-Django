# Generated by Django 2.2.5 on 2020-06-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0013_auto_20200613_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentyear',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
