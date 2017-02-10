# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from .models import JCBook

# 数据库操作
def add(request):
	one = JCBook(name='yingyu')
	one.save()
	return HttpResponse("<p>数据添加成功！</p>")

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
	#for var in list:
	#	response += var.name + " " + str(var.id) + " "
	return render(request, 'dbform.html', {'content':list})