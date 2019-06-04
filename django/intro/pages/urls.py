from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hola/', views.hola),
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello),  # defalut 값는 str
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('circle/<int:r>/', views.circle),
    path('template_language/', views.template_language),
    path('birthday/', views.birthday),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('name/', views.name),
    path('lotto/', views.lotto),
    path('lotto2/', views.lotto2),
    path('picklotto/', views.picklotto),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
