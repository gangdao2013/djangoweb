
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render
from .loginForm import LoginFormShow
from django.http import HttpResponse

def login(request):
    info = "not logged in"

    if request.method == 'POST':
        # Get the posted form
        MyLoginForm = LoginFormShow(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            example = reverse('placeholder', kwargs={'width': 50, 'height':50})
            context = {
                'good':'欢迎' + username,
                'example': request.build_absolute_uri(example)
            }
            return render(request, 'index.html', context)
        else:
            info='invalid'
    else:
        MyLoginForm = LoginFormShow()

    return HttpResponse(info)
