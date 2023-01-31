from django.shortcuts import render
from django.http import HttpResponse

app_name='hello01'

def test(request):
    return HttpResponse("<h1><a href='/'>A tag - Hello, Test!</a></h1>")


# Create your views here.
