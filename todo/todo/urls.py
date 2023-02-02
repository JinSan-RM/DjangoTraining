
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>',views.todo_list_detail, name='todo_list_detail'),
    path('post/',views.todo_post, name='todo_post'),
    path('<int:pk>',views.todo_edit, name='todo_edit'),
    path('done/',views.done_list, name='done_list'),
    path('done/<int:pk>', views.todo_done, name='todo_done'),
]