#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render
from web.forms.issues import IssuesModelForm


def issues(request, project_id):
    form = IssuesModelForm()
    return render(request, 'issues.html', {'form': form})
