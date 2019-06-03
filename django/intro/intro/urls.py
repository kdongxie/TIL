"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pages import views
import decimal
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hola/', views.hola),
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello), # defalut 값는 str
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('circle/<int:r>/', views.circle),
    path('template_language/', views.template_language),
    path('birthday/', views.birthday),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('name/', views.name),
    path('lotto/', views.lotto),
]
