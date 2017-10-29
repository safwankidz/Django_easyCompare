from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='search'),

    url(r'^result/', views.insert),

    url(r'^(?P<page_id>[0-9]+)/$',views.details, name='details'),

    url(r'^store/',views.store),

    url(r'^template/',views.template),

    url(r'^renders/$', views.renders,name='render'),
]
