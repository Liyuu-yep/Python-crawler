from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
import pandas as pd
from django.shortcuts import render

from . import models
from .models import ACG, Profile, Comments, Show


# Create your views here.


def signin(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        # 校验
        user = auth.authenticate(username=username, password=password)
        # print(user.is_superuser)
        # print(user)
        if user is not None:
            if user.is_superuser is True:
                return redirect('/import/')
            auth.login(request, user)
            return redirect('/afterlogin/')
        else:
            messages.info(request, '用户名或密码错误')
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
                # 设置默认的个人信息
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('/mainpage2/')
        else:
            messages.info(request, '两次密码不相同')
            return redirect('/signup/')
    else:
        return render(request, 'MainPage.html')


def after_login(request):
    user_profile = Profile.objects.get(user=request.user)
    # acgs = models.ACG.objects.all()[:20]
    acgs = models.ACG.objects.filter(acg_core__isnull=False).exclude(acg_core='nan').order_by('-acg_core')[:22]
    return render(request, 'AfterLogin.html', {'user_profile': user_profile, 'acgs': acgs})


def fanju_information(request):
    user_profile = Profile.objects.get(user=request.user)
    acgs = models.ACG.objects.all()
    return render(request, 'FanJuInformation.html', {"acgs": acgs, 'user_profile': user_profile})


def mainpage(request):
    return render(request, 'MainPage.html')


def password_reset_form(request):
    return render(request, './registration/password_reset_form.html')


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # 用户不存在的处理逻辑
            return redirect('reset_password')

        token = default_token_generator.make_token(user)
        reset_link = request.build_absolute_uri(
            f'/password_reset/{user.pk}/{token}/'
        )
        context = {
            'user_pk': user.pk,
            'token': token,
        }
        send_mail(
            '重置密码',
            f'请点击以下链接重置密码：{reset_link}',
            '1426438143@qq.com',
            [email],
            fail_silently=False,
        )

        # 发送邮件成功的处理逻辑
        return redirect('reset_password')

    return render(request, 'reset_password.html')


def reset_password_confirm(request, user_pk, token):
    try:
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        # 用户不存在的处理逻辑
        return redirect('reset_password')

    if not default_token_generator.check_token(user, token):
        # token验证失败的处理逻辑
        return redirect('reset_password')

    if request.method == 'POST':
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            # 两次输入的密码不一致地处理逻辑
            return redirect('reset_password_confirm', user_pk=user.pk, token=token)
        else:
            user.set_password(password)
            user.save()
            return redirect('/mainpage/')
        # 密码重置成功的处理逻辑
        # return redirect('password_reset_done')

    return render(request, 'reset_password_confirm.html', {'user_pk': user_pk, 'token': token})


def import_excel(request):
    if request.method == 'POST':
        file = request.FILES['excel_file']
        df = pd.read_excel(file)

        field_mapping = {
            '番名': 'show_name',
            '副标题': 'show_second_name',
            '链接': 'show_url',
            '追番人数': 'show_follow',
            '分数': 'show_core',
            '更新进度': 'show_progress',
            '是否完结': 'show_bool',
            '图片源': 'show_img',
        }
        # field_mapping = {
        #     '番名': 'comment_name',
        #     '评论内容': 'comment_content',
        #     '评分': 'comment_score',
        # }
        successful_imports = 0
        failed_imports = 0
        error_messages = []

        for index, row in df.iterrows():
            show = Show()
            for column, field in field_mapping.items():
                try:
                    setattr(show, field, row[column])
                except (KeyError, ValueError) as e:
                    failed_imports += 1
                    error_messages.append(f"Error importing row {index + 2}: {str(e)}")
                    break
            else:
                try:
                    show.save()
                    successful_imports += 1
                except Exception as e:
                    failed_imports += 1
                    error_messages.append(f"Error importing row {index + 2}: {str(e)}")

        # for index, row in df.iterrows():
        #     comment = Comments()
        #     for column, field in field_mapping.items():
        #         try:
        #             setattr(comment, field, row[column])
        #         except (KeyError, ValueError) as e:
        #             failed_imports += 1
        #             error_messages.append(f"Error importing row {index + 2}: {str(e)}")
        #             break
        #     else:
        #         try:
        #             comment.save()
        #             successful_imports += 1
        #         except Exception as e:
        #             failed_imports += 1
        #             error_messages.append(f"Error importing row {index + 2}: {str(e)}")

        context = {
            'successful_imports': successful_imports,
            'failed_imports': failed_imports,
            'error_messages': error_messages
        }

        return render(request, 'import_result.html', context)

    return render(request, 'import_excel.html')


def analyse(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'analyse.html', {'user_profile': user_profile})


@login_required(login_url='/signin/')
def mainpage2(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('image'):
            user_profile.profileimg = request.FILES.get('image')
            user_profile.save()
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.info(request, "用户名已存在")
        else:
            user_profile.user.username = username
            user_profile.user.save()
        return redirect('/mainpage2/')
    return render(request, 'S-MainPage2.html', {'user_profile': user_profile})


def changepassword(request):
    profile_user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.info(request, '两次密码不相同')
            return redirect('/changepassword/')
        else:
            # user.set_password(password)
            profile_user.user.set_password(password1)
            profile_user.user.save()
            return redirect('/mainpage/')
    return render(request, 'change_password.html')


def changeemail(request):
    profile_user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        if email1 != email2:
            messages.info(request, '两次邮箱不相同')
            return redirect('/changeemail/')
        else:
            # user.set_password(password)
            if User.objects.filter(email=email1).exists():
                messages.info(request, "邮箱已存在")
            else:
                profile_user.user.email = email1
                profile_user.user.save()
            return redirect('/mainpage2/')
    return render(request, 'change_email.html')


def result(request):
    # q = request.GET.get('q')
    # error_msg = ''
    # if q:
    #     post_list = ACG.objects.filter(acg_name=q)
    #     return render(request, 'result.html')
    # else:
    #     error_msg = '请输入关键字'
    #     return render(request, 'MainPage.html')
    # return render(request, 'result.html'), {'error_msg': error_msg, 'post_list': post_list}

    search_data = request.GET.get('q')
    data = models.ACG.objects.filter(acg_name__contains=search_data)
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'result.html', {"data": data, "user_profile": user_profile})
