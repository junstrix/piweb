# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("hello,world")
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
def led(request):
    """led control"""
    if 'on' in request.GET:
        """some control code"""
        return HttpResponse('led already turned on yeah')
    else:
        return render_to_response('con/led.html')
