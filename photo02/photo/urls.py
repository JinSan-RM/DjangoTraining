from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/new/', views.photo_post, name='photo_post'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
    path('photo/<int:pk>/delete/', views.photo_delete, name='photo_delete'),
    path('download/<str:filename>',views.download_proc,name='download'),
    # path('upload/',views.upload_proc,name='upload')
]