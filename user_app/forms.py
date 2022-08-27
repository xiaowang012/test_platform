# coding-utf-8
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput


# 用户登录表单
class UserForm(forms.Form):
    username = forms.CharField(min_length=1, max_length=20,
                               error_messages={"required": "用户名不能为空!", "min_length": "用户名长度不能小于1!",
                                               "max_length": "用户名长度不能大于20!"})
    password = forms.CharField(widget=PasswordInput, min_length=1, max_length=20,
                               error_messages={"required": "密码不能为空!", "min_length": "密码长度不能小于1!",
                                               "max_length": "密码长度不能大于20!"})


# 用户注册表单
class RegisterForm(forms.Form):
    username = forms.CharField(min_length=1, max_length=20,
                               error_messages={"required": "用户名不能为空!", "min_length": "用户名长度不能小于1!",
                                               "max_length": "用户名长度不能大于20!"})
    password = forms.CharField(widget=PasswordInput, min_length=1, max_length=20,
                               error_messages={"required": "密码不能为空!", "min_length": "密码长度不能小于1!",
                                               "max_length": "密码长度不能大于20!"})
    password1 = forms.CharField(widget=PasswordInput, min_length=1, max_length=20,
                                error_messages={"required": "密码不能为空!", "min_length": "密码长度不能小于1!",
                                                "max_length": "密码长度不能大于20!"})

    def clean(self):  # 全局钩子 确认两次输入的密码是否一致。
        val = self.cleaned_data.get("password")
        r_val = self.cleaned_data.get("password1")
        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("两次输入的密码不一致!")


# 用户修改密码表单
class ChangeUserPassword(forms.Form):
    old_password = forms.CharField(widget=PasswordInput, min_length=1, max_length=20,
                                   error_messages={"required": "密码不能为空!", "min_length": "密码长度不能小于1!",
                                                   "max_length": "密码长度不能大于20!"})
    new_password1 = forms.CharField(widget=PasswordInput, min_length=1, max_length=20,
                                    error_messages={"required": "密码不能为空!", "min_length": "密码长度不能小于1!",
                                                    "max_length": "密码长度不能大于20!"})
    new_password2 = forms.CharField(widget=PasswordInput, min_length=1, max_length=20,
                                    error_messages={"required": "密码不能为空!", "min_length": "密码长度不能小于1!",
                                                    "max_length": "密码长度不能大于20!"})

    def clean(self):  # 全局钩子 确认两次输入的密码是否一致。
        val = self.cleaned_data.get("new_password1")
        r_val = self.cleaned_data.get("new_password2")
        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("两次输入的密码不一致!")
