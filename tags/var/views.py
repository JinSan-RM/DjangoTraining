from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'var/index.html')

def variable01(request):
    my_list = ['python','django','template']
    return render(request, 'var/variable01.html',{'lst':my_list})

def variable02(request):
    my_dict={'name':'Kim', 'class':'AI 취업'}
    return render(request, 'var/variable02.html',{'dct':my_dict})

def testfor(request):
    return render(request, 'var/testfor.html',{'number':range(1,11)})
    #templates/var/testfor.html

def testfor01(request):
    st = [1,2,3,4,5,6,7,8,9]
    return render(request, 'var/testfor01.html',{'st':st})

def testfor02(request):
    st = [1,2,3,4,5,6,7,8,9]
    return render(request, 'var/testfor02.html',{'st':st})

def if01(request):
    return render(request,'var/if01.html',{'user':{'id':'hong-gd'}})

def if02(request):
    member = {'id': 'multi', 'class':'ai', 'role':'manager'}
    return render(request,'var/if02.html',{'member':member})

def get_post(request):
    if request.method == 'GET':
        q = request.GET['q']
        return render(request,'var/get.html',{'q':q})
    elif request.method == 'POST':
        id = request.POST['id']
        return render(request, 'var/post.html',{'id':id})

def staticTest(request):
    return render(request, 'var/staticTest.html')
