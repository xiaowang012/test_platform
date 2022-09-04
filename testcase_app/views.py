# coding=utf-8
import logging
import random

from django.shortcuts import redirect, render, HttpResponse
from . import models


# 我的testcase页面，加载当前用户下所属的所有case
def testcase_index(request):
    current_user = str(request.user)
    if request.method == 'GET':
        page_number = request.GET.get('page_number')
        try:
            page_number = int(page_number)
        except Exception as e:
            logging.INFO('参数错误: ' + str(e))
        else:
            # 返回前端的数据:当前用户，当前页码，分页样式
            dic1 = {"current_user": current_user, 'current_page': page_number}
            # 根据页码给分页加选中的样式
            if page_number > 5:
                dic1['active_next'] = 'active'
            else:
                select_page = 'active' + str(page_number)
                dic1[select_page] = 'active'
            # 根据页码查询每一页的数据
            start = 10 * (page_number - 1)
            end = 10 * page_number
            cases_data = models.TestcaseData.objects.filter(create_user=current_user)[start:end]
            for i in cases_data:
                # 给每一行添加样式
                i.style = random.choice(['error', 'info', 'success', 'warning', ''])
                # 转换时间
                i.create_time = i.create_time.strftime("%Y-%m-%d %H:%M:%S")
            return render(request, 'testcase/my_testcase.html', {"data": cases_data, "dic1": dic1})
