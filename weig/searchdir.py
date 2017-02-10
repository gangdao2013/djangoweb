# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render
import os
from .forms import AddForm

# 表单
def index(request):
	return render(request, "searchdir.html", {})

def formExample(request):
    if request.method == 'POST':# 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'searchdir.html', {'form': form})

# 接收GET请求数据
def search(request):  
	request.encoding='utf-8'
	context = {}
	if 'q' in request.GET:
				context['search_post_result'] = os.listdir(request.GET['q'])
				return render(request, 'searchdir.html', context)
	else:
				message = '你提交了空表单'
	return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
	ctx ={}
	ctx.update(csrf(request))
	if request.POST:
		ctx['search_post_result'] = os.listdir(request.POST['q'])
		return render(request, "searchdir.html", ctx)
	return HttpResponse("非法请求")
