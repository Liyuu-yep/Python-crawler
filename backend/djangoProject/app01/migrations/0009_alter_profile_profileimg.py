# Generated by Django 4.2.4 on 2023-08-18 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='../static/img/23/jpg', upload_to='profile_images'),
        ),
    ]
