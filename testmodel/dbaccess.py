# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers

from .models import JCBook
from .models import JCPerson


# 数据库操作
def addBook(request):
	request.encoding='utf-8'
	if 'name' in request.GET:
		bookName = request.GET['name']
		if not bookName:
			return HttpResponse('书名不应为空')

		ownerId = request.GET['owner']
		owner = JCPerson.objects.get(id=ownerId)
		bookId=0
		for var in JCBook.objects.order_by("id"):
			if bookId < var.id:
				bookId = var.id
		bookId += 1
		book = JCBook(id=bookId, name=request.GET['name'], owner=owner)
		book.save()
	return redirect(browse)

def addBookOwner(request):
	request.encoding='utf-8'
	if 'name' in request.GET:
		bookOwner = request.GET['name']
		if not bookOwner:
			return HttpResponse('书籍拥有者不应为空')

		owner = JCPerson.objects.filter(name=bookOwner)
		if owner:
			return HttpResponse('书籍拥有者'+bookOwner+'已存在')
		ownerId=0
		for var in JCPerson.objects.order_by("id"):
			if ownerId < var.id:
				ownerId = var.id
		ownerId += 1
		person = JCPerson(id=ownerId, name=bookOwner)
		person.save()
	return redirect(browse)

def browse(request):
	# 初始化
	response = ""

	# 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
	list = JCBook.objects.all()


	# filter相当于SQL中的WHERE，可设置条件过滤结果
	# JCBook.objects.filter(id=2)

	# 获取单个对象
	# response3 = JCBook.objects.get(id=1)

	# 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
	# JCBook.objects.order_by('name')[0:2]

	#数据排序
	# JCBook.objects.order_by("id")

	# 上面的方法可以连锁使用
	# JCBook.objects.filter(name="yingyu").order_by("id")

	# 输出所有数据
	result={}
	result['books'] = list
	result['persons'] = JCPerson.objects.all()
	#for var in list:
	#	response += var.name + " " + str(var.id) + " "
	return render(request, 'dbform.html', result)