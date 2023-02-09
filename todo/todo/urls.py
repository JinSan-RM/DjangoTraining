from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>',views.todo_list_detail, name='todo_list_detail'),
    path('post/',views.todo_post, name='todo_post'),
    path('<int:pk>/edit/',views.todo_edit, name='todo_edit'),
    path('done/',views.done_list, name='done_list'),
    path('done/<int:pk>/', views.todo_done),
    path('<int:pk>/delete/',views.todo_delete,name='delete')
]   +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)