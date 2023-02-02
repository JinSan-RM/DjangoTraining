from django.shortcuts import render, redirect
from django.utils import timezone
from .models import myboard
from django.core.paginator import Paginator

def index(request):
    myboards = myboard.objects.all().order_by('-id')

    paginator = Paginator(myboards,10) # 5개씩 paging을 합니다.
    page_num = request.GET.get('page','1') #page 값이 없으면 default 1
    page_obj = paginator.get_page(page_num) #page에 맞는 모델
    

    #총게시물 수
    print('--------------count 페이지 카운트 -----------------')
    print(page_obj.count)

    print('--------------number현재 페이지 번호----------------') 
    print(page_obj.number)                    

    print('---------------num-page 총 페이지 수-------------')
    print(page_obj.paginator.num_pages)

    print('---------------num-page 총 페이지 range객체-------------')
    print(page_obj.paginator.page_range)

    print('---------------다음 페이지, 이전페이지-------------')
    print(page_obj.has_next())
    print(page_obj.has_previous())

    try:
        print('--------------다음 페이지 숫자 없으면 에러-----------------')
        print(page_obj.next_page_number)

        print('--------------이전 페이지 숫자 없으면 에러-----------------')
        (page_obj.previous_page_number())
    except:
        pass

    print('---------------start_index--------------------------')
    print(page_obj.start_index())
    print('---------------end_index--------------------------')
    print(page_obj.end_index())


    return render(request, 'index.html/',{'myboards':page_obj}) #render 리턴값이 Httpresponse 이다.
    #return render(request, 'index.html/',{'myboards':myboards})

def insert_form(request):
    return render(request,'insert_form.html')
    
def insert_proc(request):

    mytitle = request.POST['mytitle']
    myname = request.POST['myname']
    mycontent = request.POST['mycontent']
    result = myboard.objects.create(myname=myname, mytitle=mytitle,
                                    mycontent=mycontent, mydate=timezone.now())
    # myboard.objects.create(myname='1', mytitle='1',
    #                                 mycontent='1', mydate=timezone.now())

    if result:
        return redirect('index')
        #return redirect('/')
        #http://127.0.0.1/insert_form
        #from django.shortcuts import render, redirect

    else:
        return redirect('/insert_form')
        #return redirect('insert_form')
        #http://127.0.0.1/insert_form

def detail(request, id):
    dto=myboard.objects.get(id=id)
    return render(request, 'detail.html',{'dto':dto})

def delete_proc(request, id):
    result = myboard.objects.get(id=id).delete()
    if result[0]:
       return redirect('index')
    else:
       return redirect('/detail/'+result.id)

def update_proc(request, id):
    myboards = myboard.objects.get(id=id)
    return render(request,'update_form.html',{'dto':myboards})

def updateres(request, id):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    id = request.POST['id']
    myboards = myboard.objects.filter(id=id)
    result1 = myboards.update(myname=myname)
    result2 = myboards.update(mytitle=mytitle)
    result3 = myboards.update(mycontent=mycontent)
    
    if result1 + result2 + result3 == 3:
        return redirect('detail',id=id)
    else:
        return redirect('/update_form')


