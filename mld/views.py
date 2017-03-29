from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Targets

# Create your views here.
def index(request):
    return render(request,'mld/index.html',{})

def add(request):
    if request.method == 'POST':
        descr = request.POST['txtdescr']
    return HttpResponseRedirect(reverse('mld:index',args=[]))


def addmark(request):
    return render(request,'mld/addmark.html')