from django.shortcuts import render
import os

def main(request):
    return render(request, 'index.html', {'good':'Good Luck!'})
