from django.contrib import admin
from django.urls import path
from . import views

#config/urls.py파일에 모든 요청을 받아서 분배
#config/usrls.py파일에서 guestbook/urls.py를 찾을 수 있게
urlpatterns = [
    path("", views.index),
    path("test1", views.test1),
    path("test2/<x>/<y>", views.test2),
    path("test3", views.test3)
    #def test2(request, x, y) 변수명이 같아야 함 
]
