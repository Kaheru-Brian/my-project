from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("Hello!, Welcome!!. You're at the about page.")
