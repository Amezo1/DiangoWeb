#!/usr/bin/python
#coding=utf-8 
'''
Created on 2017年7月23日

@author: qianfen
'''

from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.views.decorators import csrf

# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
#     return render_to_response(request, "search_form_post.html", ctx)
    return render(request, "search_form_post.html", ctx)

