from django.shortcuts import render, get_object_or_404, redirect
from .models import photo
from . forms import PhotoForm

# Create your views here.
def photo_list(request):
    photos = photo.objects.all()
    return render(request,'photo_list.html',{'photos':photos})

def photo_detail(request,pk):
    photos = get_object_or_404(photo,pk=pk)
    return render(request,'photo_detail.html',{'photos':photos})
    

def photo_post(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo_post.html',{'form':form})


def photo_edit(request,pk):
    photos = get_object_or_404(photo,pk=pk)

    if request.method=="GET":
        form = PhotoForm(instance=photos)
    elif request.method =='POST':
        form = PhotoForm(request.POST, instance=photos)
        if form.is_valid() :
            photos = form.save(commit=False)
            photos.save()
            return redirect('photo_detail',pk=photos.id)
        

    return render(request,'photo_post.html',{'form':form})