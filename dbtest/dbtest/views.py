from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Myboard

def index(request):
    myboard_all = Myboard.objects.all().order_by('-id') #select * from myboard
    #print(myboard_all)
    return  render(request,'index.html',{'list':myboard_all})
    #http://127.0.0.1:8000

def detail(request, id):
    return render(request,'detail.html',{'dto':Myboard.objects.get(id=id)})

def update_form(request, id): #수정버튼 클릭시 - form
    return render(request, 'update.html',{'dto':Myboard.objects.get(id=id)})

def update_proc(request):
    mycontent = request.POST['mycontent']
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    myname = request.POST['myname']

    myboard = Myboard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)
    # 성공 시 1을 리턴 함
    if result_title + result_content == 2:
        return redirect('/detail/' + id)
        # detail 가라고 request 준 것
    else:
        return redirect('/updateform/' + id)
        # updateform 가라고 request 준 것

def insert_form(request):
    return render(request,'insert.html')

def insert_proc(request):
    myname=request.POST['myname']
    mytitle=request.POST['mytitle']
    mycontent=request.POST['mycontent']

    result = Myboard.objects.create(myname=myname,mytitle=mytitle,
                            mycontent=mycontent,mydate=timezone.now())
    
    # from django.utils import timezone

    print('========================')
    print(result)
    print('========================')

    if result:
        return redirect('index')
    else:
        return redirect('insertform')

def delete_proc(request, id):
    result = Myboard.objects.filter(id=id).delete()

    print('===========DELETE=============')
    print(result)
    print('========================')

    if result[0]:
        return redirect('index')
    else:
        return redirect('/detail/'+id)