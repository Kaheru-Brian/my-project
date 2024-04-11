from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def resources(request):
    template = loader.get_template('resources.html')
    aboutresources = template.render()
    return HttpResponse (aboutresources)
