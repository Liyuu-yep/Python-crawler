from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
import pandas as pd
from django.shortcuts import render
from .models import ACG


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
                # 设置默认的个人信息
                # user_model = User.objects.get(username=username)
                # new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                # new_profile.save()
                return redirect('/afterlogin/')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('/signup/')
    else:
        return render(request, 'MainPage.html')


@login_required(login_url='/signin/')
def after_login(request):
    return render(request, 'AfterLogin.html')


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
            # 两次输入的密码不一致的处理逻辑
            return redirect('reset_password_confirm', user_pk=user.pk, token=token)

        user.set_password(password)
        user.save()

        # 密码重置成功的处理逻辑
        # return redirect('password_reset_done')

    return render(request, 'reset_password_confirm.html', {'user_pk': user_pk, 'token': token})


def import_excel(request):
    if request.method == 'POST':
        file = request.FILES['excel_file']
        df = pd.read_excel(file)

        field_mapping = {
            '番名': 'acg_name',
            '副标题': 'acg_second_name',
            '链接': 'acg_url',
            '追番人数': 'acg_follow',
            '分数': 'acg_core',
            '更新进度': 'acg_progress',
            '是否完结': 'acg_bool',
            '图片源': 'acg_img',
        }

        successful_imports = 0
        failed_imports = 0
        error_messages = []

        for index, row in df.iterrows():
            acg = ACG()
            for column, field in field_mapping.items():
                try:
                    setattr(acg, field, row[column])
                except (KeyError, ValueError) as e:
                    failed_imports += 1
                    error_messages.append(f"Error importing row {index + 2}: {str(e)}")
                    break
            else:
                try:
                    acg.save()
                    successful_imports += 1
                except Exception as e:
                    failed_imports += 1
                    error_messages.append(f"Error importing row {index + 2}: {str(e)}")

        context = {
            'successful_imports': successful_imports,
            'failed_imports': failed_imports,
            'error_messages': error_messages
        }

        return render(request, 'import_result.html', context)

    return render(request, 'import_excel.html')
