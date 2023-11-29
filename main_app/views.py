from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def pricing(request):
    return render(request, "pricing.html")


def cars(request):
    return render(request, "car.html")


def car(request):
    return render(request, "car-single.html")


def contact(request):
    return render(request, "contact.html")


def team(request):
    return render(request, 'newTeam.html')