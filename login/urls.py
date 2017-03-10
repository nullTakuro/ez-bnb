from django.conf.urls import url
from . import views

# Each url is linked to a views return
urlpatterns = [
    #/login/
    url(r'^$', views.index, name='index'),   #default home page for the login page
]
