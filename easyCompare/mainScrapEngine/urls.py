from django.conf.urls import url
from . import views

app_name = 'mainScrapEngineS'

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^result/', views.insert),

    url(r'^(?P<page_id>[0-9]+)/$',views.details, name='details'),

    url(r'^store/',views.store),

    url(r'^renders/$', views.renders,name='render'),
]
