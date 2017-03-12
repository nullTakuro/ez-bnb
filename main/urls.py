from django.conf.urls import url
from . import views

# Each url is linked to a views return
urlpatterns = [
    #/login/
    url(r'^login/$', views.index, name='index'),   #default home page for the login page
    #/bookings/id="corresponding ID"
    url(r'^bookings/id=(?P<bookingID>[0-9]+)/$', views.bookingRender, name='bookingRender'),
]
