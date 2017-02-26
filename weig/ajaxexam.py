# -*- coding: utf-8 -*-

from django.http import JsonResponse
import json

def test_ajax(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def test_ajax_post(request):
    val=request.POST['persons']
    conts=json.loads(val)
    dd=[]
    for i in conts:
        dd.append({'name':i['name'],'Age':i['age']+1})
    return JsonResponse({'info':dd})
