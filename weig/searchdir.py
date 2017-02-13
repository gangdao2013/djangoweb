# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
import os

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
