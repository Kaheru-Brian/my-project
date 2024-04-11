from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Index(request):
    template = loader.get_template('index.html')
    homecontent = template.render()
    return HttpResponse(homecontent)
