from django.shortcuts import render
from app.models import *

# Create your views here.

def index(request):
    info = Info.objects.all()
    projects = Projects.objects.all()
    context = {'info':info,
               'projects':projects
        }
    return render(request,'index.html',context)


