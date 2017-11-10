from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^(?P<page_id>[0-9]+)/$',views.details, name='details'),

    url(r'^(?P<URLstrip>[-\w+\d+]+)/$',views.specs, name='spec'),

    #url(r'^test/$',views.specs),

    #url(r'^store/',views.store),

    #url(r'^result/', views.insert),

    #url(r'^renders/$', views.renders,name='render'),

]
