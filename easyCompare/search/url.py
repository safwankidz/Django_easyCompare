from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^result/', views.insert),

    url(r'^(?P<page_id>[0-9]+)/$',views.details, name='details'),

    #navigate to product page - in progress
    url(r'^search/(?P<title>[\w-]+)/$',views.specs, name='spec'),

    url(r'^store/',views.store),

    url(r'^renders/$', views.renders,name='render'),

    #url(r'^template/',views.template),
]
