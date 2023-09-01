from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index , name='home'),
    path("first",views.first,name='first'),
    path("about", views.about , name='about'),
    path("acadmics", views.acadmics , name='acadmics'),
    path("contact", views.contact , name='contact'),
    
]
