from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

User = get_user_model()


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profile_img = models.ImageField(upload_to='profile_images', default='img.png')
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



