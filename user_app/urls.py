# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("password/",views.change_password),
    path("login/",views.login),
    path("logout/",views.logout),
    path("password/",views.change_password),
    path("register/",views.register),
]
