#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms

from web import models
from web.forms.bootstrap import BootStrapForm


class WikiModelForm(BootStrapForm, forms.ModelForm):
    class Meta:
        model = models.Wiki
        exclude = ['project', ]
