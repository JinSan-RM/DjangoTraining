from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
# Create your views here.

def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    paginator = Paginator(todos,10)
    page_num = request.GET.get('page','1')
    page_obj = paginator.get_page(page_num)
    return render(request, 'todo/todo_list.html',{'todos':todos, 'todos':page_obj})

def todo_list_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_list_detail.html',{'todo':todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            if 'imagefile' in request.FILES.dict():
                upload_file = request.FILES['imagefile']
                upload = default_storage.save(upload_file.name, ContentFile(upload_file.read()))
                # default_storage = /media, 파일 업로드 가능
                Todo.objects.filter(id=todo.id).update(imagefile=upload_file) # 신규로 저장한 todo의 id를 참조해서 imagefile의 값을 update함
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html',{'form':form})

def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form':form})

def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/todo_done_list.html', {'dones':dones})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('/done/', {'todo':todo})

def todo_delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect('todo_list')
