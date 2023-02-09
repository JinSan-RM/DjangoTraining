from django.shortcuts import render,redirect
from .forms import MemberForm, LoginForm
from .models import Member
from django.contrib.auth import login as django_login,logout as django_logout
from django.contrib.auth import authenticate
from django.http import HttpResponse
# Create your views here.
def login(request):
    login_form = LoginForm()
    return render(request,'users/login.html',{'login_form':login_form})

def loginProcess(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        username=login_form.data['username']
        password=login_form.data['password']

        user = authenticate(username=username,password=password)
        #장고에서 로그인 성공여뷰를 확인해줌

        if user is not None:    #성공
            django_login(request, user)
            return redirect('home')
        else:
            return redirect('login')

def logout(request):
    django_logout(request)
    return redirect('home')


def signup(request):
    member_form = MemberForm()
    return render(request,'users/signup.html',{'member_form':member_form})

def signup_process(request):
    if request.method == "POST":
        member_form = MemberForm(request.POST)
        if member_form.is_valid():
            if 'image' in request.FILES.keys(): #이미지첨부된 경우
                new_user = Member.objects.create_user(
                    username = member_form.cleaned_data['username'], #validation이 완료된 데이터
                    email=member_form.cleaned_data['email'],
                    password=member_form.cleaned_data['password1'],
                    mobile=member_form.cleaned_data['mobile'],
                    image=request.FILES['image']
                )

            else: # 이미지 첨부 안됨
                new_user = Member.objects.create_user(
                    username = member_form.cleaned_data['username'], #validation이 완료된 데이터
                    email=member_form.cleaned_data['email'],
                    password=member_form.cleaned_data['password1'],
                    mobile=member_form.cleaned_data['mobile'],
                )

            # from django.contrib.auth import login as django_login
            # 로그인 세션처리 함
            django_login(request,new_user)
            return redirect('home')
        else:
            return redirect('users:signup')
