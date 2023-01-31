from django.shortcuts import render


def index(request):
    return render(request,'tags/index.html',{'name':'Kim Jin San'})
    #BASE_DIR : project_name/templates/tags/index.html
    # project_name/templates/tags/index.html