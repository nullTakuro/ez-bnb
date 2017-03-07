from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),   #difault home page for the login page
]
