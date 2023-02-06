"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import HelloAPI, bookAPI, booksAPI, BooksAPI, BookAPI
from django.urls import path, include


urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/books/',booksAPI),            # 함수형 뷰의 booksAPI 연결
    path('fbv/book/<int:bid>/', bookAPI),   # 함수형 뷰의 bookAPI 연결
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view())
]
