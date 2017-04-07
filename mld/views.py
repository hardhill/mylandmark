from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Targets


# Create your views here.
def index(request):
    return render(request, 'mld/index.html', {})


# добавление маркера в БД
def add(request):
    """добавление маркера"""
    if request.method == 'POST':
        descr = request.POST['txtdescr']
        lng = request.POST['txtlng']
        lat = request.POST['txtlat']
        if descr and lng and lat:
            t = Targets(description=descr, longitude=lng, latitude=lat)
            t.save(force_insert=True)

        else:
            html = '<p>Ошибка: параметры имеют пустое значение</p>'
            return HttpResponse(html)

    return HttpResponseRedirect(reverse('mld:viewmark'))


def update(request):
    """обновление значений данных Таргетс"""
    if request.method == 'POST':
        descr = request.POST['txtdescr']
        lng = request.POST['txtlng']
        lat = request.POST['txtlat']
        idmarker = request.POST['id']
        if descr:
            t = Targets.objects.get(id=idmarker)
            if t:
                t.description = descr
                t.latitude = lat
                t.longitude = lng
                t.save()
        return HttpResponseRedirect(reverse('mld:viewmark'))


def delmarker(request):
    """удаление конкретного маркера из таблицы"""
    if request.method == 'POST':
        idmarker = request.POST['id']
        if not idmarker == None:
            t = Targets.objects.filter(id=idmarker).delete();
    return HttpResponseRedirect(reverse('mld:viewmark'))


def addmark(request):
    return render(request, 'mld/addmark.html')


def viewmark(request):
    markers = Targets.objects.all().order_by('created_dt')
    context = {'markers': markers}
    return render(request, 'mld/viewmark.html', context)
