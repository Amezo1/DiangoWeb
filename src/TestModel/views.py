# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from models import Test

def hello(request):
#     return HttpResponse("Hello world ! ")
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def usetemplate(request):
    context          = {}
    context['user'] = '大饼'
    context['hello'] = 'Hello World!'
    return render(request, 'usetemplate.html', context)

 
# 数据库操作insert操作
def dbinsert(request):
    test1 = Test(name='mimi',age=8)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

# 数据库操作
def dbselect(request):
    # 初始化
    response = ""
    response1 = ""
    
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1) 
    
    # 获取单个对象
    response3 = Test.objects.get(id=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]
    
    #数据排序
    Test.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")

def dbupdate(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'wunaihui/qianfen-mimi-dabing'
    test1.age = 99999
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse("<p>修改成功</p>")

def dbdelete(request):
    # 删除id=1的数据
    try:
        test1 = Test.objects.get(id=2)
        test1.delete()
    except Test.DoesNotExist,e:
        print e
    
    # 另外一种方式
    # Test.objects.filter(id=2).delete()
    
    # 删除所有数据
    # Test.objects.all().delete()
    
    return HttpResponse("<p>删除成功</p>")
