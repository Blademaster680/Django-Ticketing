from django.shortcuts import render
from django.contrib.auth.models import User
from apps.ticketing.models import Ticket, Comment

# Create your views here.
def dashboard(request):

    context = {
        'users': User.objects.all(),
        'tickets': Ticket.objects.all(),
    }

    return render(request, 'dashboard/dashboard.html', context)