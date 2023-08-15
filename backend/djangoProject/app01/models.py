from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

User = get_user_model()


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    # 个人简介


