from bs4 import BeautifulSoup
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend, UserModel
from django.views import View

from . import models


# Create your views here.


def signin(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        # 校验
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/ranklist/')
        else:
            messages.info(request, '登陆失败')
            return redirect('/signin/')
    else:
        return render(request, 'MainPage.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password2 == password:
            # 邮箱已经存在
            if User.objects.filter(email=email).exists():
                messages.info(request, "邮箱已存在")
                return redirect('/signup/')
            # 用户名已经存在
            elif User.objects.filter(username=username).exists():
                messages.info(request, "用户名已存在")
                return redirect('/signup/')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # 登录
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                # # 设置默认的个人信息
                # user_model = User.objects.get(username=username)
                # new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                # new_profile.save()
                return redirect('/ranklist/')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('/signup/')
    else:
        return render(request, 'MainPage.html')


def after_login(request):
    return render(request, 'ranking-list-1.html')


def rank_list(request):
    return render(request, 'ranking-list.html')


def fanju_information(request):
    return render(request, 'FanJuInformation.html')


def mainpage(request):
    return render(request, 'MainPage.html')


def mainpage1(request):
    return render(request, 'S-MainPage.html')


def mainpage2(request):
    return render(request, 'S-MainPage2.html')


def self_mainpage(request):
    return render(request, 'Self-MainPage.html')

