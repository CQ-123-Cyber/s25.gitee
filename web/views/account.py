#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
用户账户相关功能：注册、短信、登录、注销
"""
from django.shortcuts import render, HttpResponse
from web.forms.account import RegisterModelForm, SendSmsForm




def register(request):
    """ 注册 """
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})


def send_sms(request):
    """ 发送短信 """
    form = SendSmsForm(request, data=request.GET)
    # 只是校验手机号：不能为空、格式是否正确
    if form.is_valid():
        pass
    return HttpResponse('成功')
