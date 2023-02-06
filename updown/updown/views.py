from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def upload_proc(requst):
    upload_file = requst.FILES['uploadfile']
    upload = default_storage.save(upload_file.name,
        ContentFile(upload_file.read()))

    return render(requst, 'download.html',{'filename':upload})    
    #default_storage : setting.py에서 설정한 MEDIA_ROOT = BASE_DIR/
    #upload_file.name : random을 파일명에 더해서 올림 (덮어쓰여지지 않음)

def download_proc(request, filename):
    return HttpResponse(default_storage.open(filename).read(),
        content_type='application/force-download')

        #content-type = 'application/force-download' => 다운로드 할 수 있게 해주는것