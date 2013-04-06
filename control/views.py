#coding=utf-8
# Create your views here.
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

def index(request):
    led_center = "RasPi Control Center"
    current_time = datetime.today()
    return render_to_response('con/led.html',{'led_center':led_center,
        'current_time':current_time})
def login_view(request):
    """user login page"""
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/control/control/')
    else:
        return HttpResponseRedirect('/control/invalid/')

def logout_view(request):
    """user logout page"""
    auth.logout(request)
    return HttpResponseRedirect('/control/logedout/')

def tform(request):
    if request.POST.has_key('uname'):
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        return HttpResponse('you has logged')
    else:
        return render_to_response('con/test.html')

def search_form(request):
    """search-form get method test"""
    return render_to_response('con/search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You search for : %r' % request.GET['q']
    else:
        message = 'you submitted an empty form.'
    return HttpResponse(message)

def login(request):
    led_center = "用户登录"
    current_time = datetime.today()
    return render_to_response('con/login.html',{'led_center':led_center,'current_time':current_time})

def control(request):
    """get a post control gpio"""
    led_center="raspberry pi control"
    current_time = datetime.today()
    light_bol = "/static/eg_bulboff.gif"
    light_status = "on"
    if not request.user.is_authenticated():
        return HttpResponse("你无权访问...")
    if request.POST.get('l_status','') == 'on':
        light_bol = "/static/eg_bulbon.gif"
        light_status = "off"
    return render_to_response('con/control.html',{'led_center':led_center,'current_time':current_time,'light_bol':light_bol,'light_status':light_status})
def test(request):
    """test"""
    if request.POST.get('l_status','') == 'on':
        return HttpResponse("success!")
    else:
        return HttpResponse("failed!")
