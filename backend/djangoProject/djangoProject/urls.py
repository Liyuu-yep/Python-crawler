"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('signup/', views.signup),

    path('signin/', views.signin),

    path('afterlogin/', views.after_login),

    path('ranklist/', views.rank_list),

    path('fanjuinformation/', views.fanju_information),

    path('mainpage/', views.mainpage),

    path('mainpage1/', views.mainpage1),

    path('mainpage2/', views.mainpage2),

    path('selfmainpage/', views.self_mainpage),

    path('password_reset/', views.reset_password, name='reset_password'),

    path('password_reset/<int:user_pk>/<str:token>/', views.reset_password_confirm, name='reset_password_confirm'),

    path('import/', views.import_excel, name='import_excel'),
]
