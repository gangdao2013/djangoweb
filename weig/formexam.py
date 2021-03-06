# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddForm

def formExample(request):
    if request.method == 'POST':# 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'formExam.html', {'form': form})

def formExample2(request):
    if request.method == 'POST':# 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            result = str(a) + "+" + str(b) + "=" + str(int(a) + int(b))
            return render(request, 'formExam.html', {'sumResult': result})
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'formExam.html', {'form': form})