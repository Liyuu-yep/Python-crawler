# Generated by Django 4.2.4 on 2023-08-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_alter_profile_profileimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=50)),
                ('comment_content', models.CharField(max_length=5000)),
                ('comment_score', models.IntegerField(max_length=10)),
            ],
        ),
    ]