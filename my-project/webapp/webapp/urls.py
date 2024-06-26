"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import Index 
from about.views import about
from contacts.views import contacts
from resources.views import resources
from blog.views import blog
from authentication.views import loginview, registerview

urlpatterns = [
    path("", Index, name="Index"),
    path("about/", about, name="About"),
    path("contacts/", contacts, name="ContactUs"),
    path("resources/", resources, name="resources" ),
    path("blog/", blog, name="blog" ),
    path("student_login/", loginview, name="login"),
    path("student_register/", registerview, name="register"),
    
    

]
