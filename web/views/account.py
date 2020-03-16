#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
用户账户相关功能：注册、短信、登录、注销
"""
from django.shortcuts import render, HttpResponse
from web.forms.account import RegisterModelForm


def register(request):
    """ 注册 """
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})


def send_sms(request):
    """ 发送短信 """
    print(request.GET)

    return HttpResponse('成功')
