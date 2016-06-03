# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


#注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            #添加到数据库
            User.objects.create(username=username, password=password)
            return HttpResponse('regist success')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf':uf}, context_instance=RequestContext(request))



#登录
def login(request):
    if request.method == 'POST':
        print('111111111')
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            user = User.objects.filter(username__exact = username, password__exact = password)
            if user:
                response = HttpResponseRedirect('/online/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/online/login/')

    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf':uf}, context_instance=RequestContext(request))


def index(request):
    username = request.COOKIES.get('username','')
    if username:
        return render_to_response('index.html', {'username':username})
    else:
        return render_to_response('login.html', {'uf':uf}, context_instance=RequestContext(request));



def logout(request):
    response = HttpResponse('logoout!')
    response.delete_cookie('username')
    return response
