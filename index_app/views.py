# coding=utf-8
from django.shortcuts import redirect, render
from . import forms


# 主页
def index(request):
    current_user = request.user
    if request.method == "GET":
        data = {"current_user": current_user}
        return render(request, "index/index.html", {"dic1": data})
