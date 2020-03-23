#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.urls import reverse
from web.forms.wiki import WikiModelForm


def wiki(request, project_id):
    """ wiki的首页 """

    return render(request, 'wiki.html')


def wiki_add(request, project_id):
    """ wiki添加 """
    if request.method == 'GET':
        form = WikiModelForm()
        return render(request, 'wiki_add.html', {'form': form})
    form = WikiModelForm(request.POST)
    if form.is_valid():
        form.instance.project = request.tracer.project
        form.save()
        url = reverse('wiki', kwargs={'project_id': project_id})
        return redirect(url)

    return render(request, 'wiki_add.html', {'form': form})
