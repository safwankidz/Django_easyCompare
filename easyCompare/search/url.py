from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^$', views.result, name='result'),

    url(r'^(?P<page_id>[0-9]+)/$',views.details, name='details'),

    url(r'^(?P<URLstrip>[-\w+\d+]+)/$',views.specs, name='spec'),

]
