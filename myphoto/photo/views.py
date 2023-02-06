from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from . forms import PhotoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all()
    return render(request,'photo_list.html',{'photos':photos})

def photo_detail(request,pk):
    photos = get_object_or_404(Photo,pk=pk)
    return render(request,'photo_detail.html',{'photos':photos})
    

def photo_post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        
        if form.is_valid():

            photo = form.save(commit=False)
            photo.save()
            upload_file = request.FILES['imagefile']       
            default_storage.save(upload_file.name, ContentFile(upload_file.read()))
            Photo.objects.filter(id=photo.id).update(imagefile=upload_file)
            return redirect('photo_detail', pk=photo.id)

    else:
        form = PhotoForm()
    return render(request, 'photo_post.html', {'form': form})


def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST,instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()

            upload_file = request.FILES['imagefile']
            default_storage.save(upload_file.name, ContentFile(upload_file.read()))
            Photo.objects.filter(id=pk).update(imagefile=upload_file)

            return redirect('photo_detail', pk=photo.pk)
           
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form': form})

def delete_proc(request,pk):
    result = Photo.objects.filter(id=pk).delete()

    return redirect('photo_list')

def download_proc(request,filename):
    return HttpResponse(default_storage.open(filename).read(),
        content_type='application/force-downlaod')

def upload_proc(request):
    pass