from django.conf.urls import url
from . import views

# Each url is linked to a views return
urlpatterns = [
    #/login/
    url(r'^$', views.index, name='index'),   #difault home page for the login page
    #https://www.youtube.com/watch?v=mWofrhTwGWQ
]
