from django.urls import path
from . import views

app_name='bbs'
#127.0.0.1:8000/bbs/

urlpatterns = [
    path('list/',views.b_list,name='b_list'),
    path('create/',views.b_create,name='b_create'),
    # form, DB저장, GET/POST
    path('<int:board_id>/detail/',views.b_detail,name='b_detail'),
    path('<int:board_id>/update/',views.b_update,name='b_update'),
    path('<int:board_id>/updateProcess/',views.b_update_process,name='b_update_process'),
    path('<int:board_id>/like/',views.b_like,name='b_like'),
    path('<int:board_id>/delete/',views.b_delete,name='b_delete'),
    path('commnetCreate/',views.c_create,name='c_create'),


]