# coding=utf-8
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from . import forms
import os


# 判断是否处于登录状态，登录状态跳转首页，否则跳转登录页
def host(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    else:
        return redirect('/user/login/')


# 用户登录
def login(request):
    if request.method == "GET":
        return render(request, "user/login.html")
    elif request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            # 密码校验
            login_user_obj = auth.authenticate(username=username, password=password)
            if not login_user_obj:
                # 定义密码错误信息
                dic1 = {'message': '用户名或密码错误!'}
                return render(request, "user/login.html", {"form": form, "dic1": dic1})
            else:
                request.session["is_login"] = True
                auth.login(request, login_user_obj)
                return redirect('/index/home/')
        else:
            return render(request, "user/login.html", {"form": form})


# 用户注册
def register(request):
    if request.method == "GET":
        return render(request, "user/register.html")
    elif request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            password1 = request.POST.get("password1")
            if password == password1:
                if not User.objects.filter(username=username).first():
                    # 用户名查重,如果查不到，正常创建用户
                    try:
                        User.objects.create_user(username=str(username), password=str(password))
                    except Exception as e:
                        # 返回对应的错误提示信息到页面
                        message = ' 注册: ' + str(username) + ' Failed!'
                        data = {'frame_type': 'alert alert-dismissable alert-danger',
                                'title': 'ERROR ',
                                'message': message
                                }
                        return render(request, 'user/register.html', {'form': form, 'dic1': data})
                    else:
                        # 返回对应的注册成功提示信息到页面
                        message = ' 注册: ' + str(username) + ' SUCCESS!'
                        # 创建对应的测试代码目录./TestCodeBase/testcase_username/main.py
                        testcase_path = os.getcwd()+ os.sep+'TestCodeBase'+os.sep + 'testcase_' + str(username)

                        os.mkdir(testcase_path)
                        data = {'frame_type': 'alert alert-success alert-dismissable',
                                'title': 'SUCCESS ',
                                'message': message}
                        return render(request, 'user/register.html', {'form': form, 'dic1': data})
                else:
                    error = '用户: ' + str(username) + ' 已存在! 请不要重复注册!'
                    data = {'frame_type': 'alert alert-dismissable alert-danger',
                            'title': 'ERROR ',
                            'message': error
                            }
                    return render(request, "user/register.html", {"form": form, "dic1": data})
            else:
                error_msg = '两次输入的密码不一致!'
                data = {'frame_type': 'alert alert-dismissable alert-danger',
                        'title': 'ERROR ',
                        'message': error_msg
                        }
                return render(request, "user/register.html", {"form": form, "dic1": data})
        else:
            # 未通过表单验证
            clear_err = form.errors.get('__all__')
            if clear_err:
                clear_err = str(clear_err).replace('<ul class="errorlist nonfield"><li>', '').replace('</li></ul>', '')
            data = {'frame_type': 'alert alert-dismissable alert-danger',
                    'title': 'ERROR ',
                    'message': clear_err
                    }
            return render(request, "user/register.html", {"form": form, 'dic1': data})


# 用户登出
# @login_required
# @permission_check
def logout(request):
    auth.logout(request)
    return redirect('/user/login/')


# 用户修改密码
def change_password(request):
    current_user = request.user
    if request.method == "GET":
        data = {"current_user": str(current_user)}
        return render(request, "user/password.html", {"dic1": data})
    elif request.method == "POST":
        form = forms.ChangeUserPassword(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            old_password = request.POST.get("old_password")
            new_password1 = request.POST.get("new_password1")
            new_password2 = request.POST.get("new_password2")
            login_user_obj = auth.authenticate(username=username, password=old_password)
            if not login_user_obj:
                # 定义密码错误信息
                data = {'message': '原密码错误!修改失败!',
                        'frame_type': 'alert alert-dismissable alert-danger',
                        'title': 'Failed',
                        'current_user': str(current_user)
                        }
                return render(request, "user/password.html", {"form": form, "dic1": data})
            if new_password1 == new_password2:
                # 修改密码
                login_user_obj.set_password(new_password1)
                login_user_obj.save()
                message = ' 修改密码成功! 请使用新密码登录! '
                data = {'frame_type': 'alert alert-success alert-dismissable',
                        'title': 'SUCCESS ',
                        'message': message,
                        'current_user': str(current_user)
                        }
                return render(request, 'user/password.html', {'form': form, 'dic1': data})
            else:
                data = {'message': '两次输入的密码不一致!',
                        'frame_type': 'alert alert-dismissable alert-danger',
                        'title': 'Failed',
                        'current_user': str(current_user)
                        }
                return render(request, "user/password.html", {"form": form, "dic1": data})
        else:
            # 未通过表单验证
            clear_err = form.errors.get('__all__')
            if clear_err:
                clear_err = str(clear_err).replace('<ul class="errorlist nonfield"><li>', '').replace('</li></ul>', '')
            data = {'message': clear_err,
                    'frame_type': 'alert alert-dismissable alert-danger',
                    'title': 'Failed',
                    'current_user': str(current_user)
                    }
            return render(request, "user/password.html", {"form": form, "dic1": data})
