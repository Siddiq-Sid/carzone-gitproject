from django.shortcuts import render
from teams.models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request,'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request,'pages/about.html', data)

def services(request):
    return render(request,'pages/services.html', data)

def contact(request):
    return render(request,'pages/contact.html', data)