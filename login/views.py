from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    all_users = User.objects.all()
    

    return HttpResponse("<h1> This is the login page!</h1>")

def bookingRender(request, bookingID):
    return HttpResponse("<h1> Booking Render for " + str(bookingID) + "</h1>")
