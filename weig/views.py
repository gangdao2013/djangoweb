
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .loginForm import LoginFormShow
from django.http import HttpResponse
import os

def main(request):
    return render(request, 'index.html', {'good':'Good Luck!'})

def login(request):
    info = "not logged in"

    if request.method == 'POST':
        # Get the posted form
        MyLoginForm = LoginFormShow(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            return render(request, 'index.html', {'good': '欢迎' + username})
        else:
            info='invalid'
    else:
        MyLoginForm = LoginFormShow()

    return HttpResponse(info)
