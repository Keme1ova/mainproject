from django.shortcuts import render
from cars.models import Premium, Jeep, Limousine, Cabriolets, Retro, Transfer
from . import models

def home(request):
    cars = models.Cards.objects.all()
    descriptions = models.About_us.objects.all()[:1]
    coms = models.Feedback.objects.all()[:2]
    footer = models.Footer.objects.all()[:1]

    context = {
        'cars': cars,
        'descriptions' : descriptions,
        'coms' : coms,
        'footer' : footer,
    }
    return render(request, 'home.html', context)




def catalog1(request):
    premium = Premium.objects.all()

    return render(request, 'premium.html', {'premium': premium})


def catalog2(request):
    jeep = Jeep.objects.all()

    return render(request, 'jeep.html', {'jeep':jeep })


def catalog3(request):
    limousine = Limousine.objects.all()

    return render(request, 'limousene.html', {'limousine':limousine})


def catalog4(request):
    cabriolets = Cabriolets.objects.all()

    return render(request, 'cabriolets.html', {'cabriolets': cabriolets})


def catalog5(request):
    retro = Retro.objects.all()

    return render(request, 'retro.html', {'retro':retro })


def catalog6(request):
    transfer = Transfer.objects.all()

    return render(request, 'transfer.html', {'transfer': transfer})


