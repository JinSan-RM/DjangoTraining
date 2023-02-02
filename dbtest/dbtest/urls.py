"""dbtest URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    #http://127.0.0.1:8000
    path('detail/<int:id>',views.detail),
    path('updateform/<int:id>',views.update_form, name='updateform'),
    path('updateres/',views.update_proc, name='updateres'),
    # 클릭 (id가 없는 이유는 request post(hidden))로 전달
    path('insertform/',views.insert_form, name='insertform'),
    path('insertres/',views.insert_proc, name='insertres'),
    path('deleteres/<int:id>',views.delete_proc, name='deleteres'),
]
