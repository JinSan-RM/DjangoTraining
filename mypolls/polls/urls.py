from django.urls import path
from . import views
app_name = 'polls'
#http://127.0.0.1:8000/polls/~~~
urlpatterns = [
    path('',views.index, name='index'),
    #http://127.0.0.1:8000/polls/index                  : 질문리스트
    path('<int:question_id>/',views.detail,name='detail'),
    ##http://127.0.0.1:8000/polls/숫자                  : 초이스 리스트 form
    path('<int:question_id>/vote/',views.vote,name='vote'),
    #http://127.0.0.1:8000/polls/숫자/vote              : 선택한 것을 DB에 저장
    path('<int:question_id>/result/',views.result,name='result'),
    #http://127.0.0.1:8000/polls/숫자/result            : 결과 보여주기

]