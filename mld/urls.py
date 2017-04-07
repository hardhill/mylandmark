# filename urls
# author hardh
# datetime 27.03.2017 - 22:14
from django.conf.urls import url

from mld import views

app_name = 'mld'
urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^addmark/',views.addmark, name='addmark'),
    url(r'^add/',views.add),
    url(r'^viewmark/',views.viewmark,name='viewmark'),
    url(r'^del/',views.delmarker),
    url(r'^update/',views.update),
]