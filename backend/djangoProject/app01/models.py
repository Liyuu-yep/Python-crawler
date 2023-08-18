from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

User = get_user_model()


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to='profile_images', default='../static/img/23.jpg')
    # 个人简介


class ACG(models.Model):
    acg_name = models.CharField(max_length=50)
    acg_second_name = models.CharField(max_length=50)
    acg_url = models.URLField()
    acg_follow = models.CharField(max_length=50)
    acg_core = models.CharField(max_length=50, null=True, blank=True)
    acg_progress = models.CharField(max_length=50)
    acg_bool = models.BooleanField(default=True)
    acg_img = models.URLField()


class Comments(models.Model):
    comment_name = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=5000)
    comment_score = models.IntegerField(max_length=10)


class Show(models.Model):
    show_name = models.CharField(max_length=60)
    show_second_name = models.CharField(max_length=50)
    show_url = models.URLField()
    show_follow = models.CharField(max_length=50)
    show_core = models.CharField(max_length=50, null=True, blank=True)
    show_progress = models.CharField(max_length=50)
    show_bool = models.BooleanField(default=True)
    show_img = models.URLField()
