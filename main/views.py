from django.http import HttpResponse
from django.template import loader
from .models import user

# Create your views here.

def index(request):
    all_users = user.objects.all()
    template = loader.get_template('main/index.html')
    context = {                         # Setting up a dictionary.
        'all_users' : all_users,
    }
    return HttpResponse(template.render(context, request))

def bookingRender(request, bookingID):
    return HttpResponse("<h1> Booking Render for " + str(bookingID) + "</h1>")
