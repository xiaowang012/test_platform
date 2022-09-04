# coding=utf-8
from django.db import models
from django.db.models.fields import AutoField, IntegerField, CharField, BooleanField
from django.utils import timezone
from django.db.models import DateTimeField


# testcase 数据库模型
class TestcaseData(models.Model):
    id = AutoField(primary_key=True)
    case_name = CharField(max_length=50)
    case_description = CharField(max_length=200)
    create_user = CharField(max_length=50)
    create_time = DateTimeField(default=timezone.now)
    case_status = BooleanField()
    project_id = IntegerField(default=0)
    code_resource_address = CharField(max_length=200)


# projects项目表
class Projects(models.Model):
    id = AutoField(primary_key=True)
    project_name = CharField(max_length=100)
    project_description = CharField(max_length=200)
    create_user = CharField(max_length=50)
    create_time = DateTimeField(default=timezone.now)
    project_status = BooleanField()
