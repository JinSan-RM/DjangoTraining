from django.contrib import admin
from django.urls import path, include
from . import views

app_name:'var'
urlpatterns = [
    path('', views.index),
    #http://127.0.0.1/var
    path('var01/',views.variable01),
    #http://127.0.0.1/var/var01
    path('var02/',views.variable02),
    #http://127.0.0.1/var/var02
    path('for/',views.testfor),
    #http://127.0.0.1/var/for
    path('for01/',views.testfor01),
    #http://127.0.0.1/var/for01
    path('for02/',views.testfor02),
    #http://127.0.0.1/var/for02
    path('if01/',views.if01),
    #http://127.0.0.1/var/if01
    path('if02/',views.if02),
    #http://127.0.0.1/var/if02
    path('req/',views.get_post),
    #http://127.0.0.1/var/req
    path('statics/',views.staticTest),
    #http://127.0.0.1/var/staticTest

]