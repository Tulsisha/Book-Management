"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from.import views

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('page1',views.page1),
    path('Premchand',views.Premchand),
    path('Tagore',views.Tagore),
    path('Arundhati',views.Arundhati),
    path('biography',views.biography),
    path('login',views.login1),
    path('contactm',views.contactM),
    path('change',views.change),
    path('changepassword',views.changepassword),
    path('home',views.home),
    path('loginform',views.loginform),
    path('all',views.all),
    path('delete',views.delete),
    path('erase',views.erase),
    path('update',views.update),
    path('userupdate',views.userupdate),
    path('search',views.search),
    path('usersearch',views.usersearch),
    path('userlogout',views.userlogout),
    path('permanent',views.permanent),
    
]
