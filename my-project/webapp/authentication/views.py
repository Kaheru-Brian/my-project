from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def loginview(request):
    template = loader.get_template('login.html')
    logincontent = template.render()
    return HttpResponse(logincontent)



def registerview(request):
    template = loader.get_template('register.html')
    registercontent = template.render()
    return HttpResponse(registercontent)
