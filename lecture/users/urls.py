from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
#http://127.0.0.1/users
app_name='users'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('signupProcess/',views.signup_process,name='signupProcess'),
    path('logout/',views.logout,name='logout'),
    path('loginProcess/',views.loginProcess,name='loginProcess'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    #js, css, image 정적 파일관리 (Django가 webserver 역할을 함)
