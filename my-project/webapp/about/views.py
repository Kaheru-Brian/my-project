from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def about(request):
    template = loader.get_template('aboutus.html')
    aboutcontent = template.render()
    return HttpResponse(aboutcontent)
