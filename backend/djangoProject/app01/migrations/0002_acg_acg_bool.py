# Generated by Django 4.2.4 on 2023-08-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acg',
            name='acg_bool',
            field=models.BooleanField(default=True),
        ),
    ]
