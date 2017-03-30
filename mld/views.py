from django.http import  HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Targets

# Create your views here.
def index(request):
    return render(request,'mld/index.html',{})

# добавление маркера в БД
def add(request):
    if request.method == 'POST':
        descr = request.POST['txtdescr']
        lng = request.POST['txtlng']
        lat = request.POST['txtlat']
        if descr and lng and lat:
            t = Targets(description=descr,longitude=lng,latitude=lat)
            t.save(force_insert=True)
            html = '<p>Данные добавлены :</p><p>' + descr + '</p><p>' + lng + '</p><p>' + lat + '</p>'
        else:
            html = '<p>Ошибка: параметры имеют пустое значение</p>'

    return HttpResponse(html)


def addmark(request):
    return render(request,'mld/addmark.html')


def viewmark(request):
    markers = Targets.objects.all().order_by('created_dt')
    context = {'markers':markers}
    return render(request,'mld/viewmark.html',context)