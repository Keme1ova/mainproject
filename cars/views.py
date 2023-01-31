from django.shortcuts import render
from . import models

def catalog1(request):
    premium = models.Premium.objects.all()

    return render(request, ' premium.html', {'premium': premium})


def catalog2(request):
    jeep = models.Jeep.objects.all()

    return render(request, 'jeep.html', {'jeep':jeep })


def catalog3(request):
    limousine = models.Limousine.objects.all()

    return render(request, 'limousine .html', {'limousine':limousine })


def catalog4(request):
    cabriolets = models.Cabriolets.objects.all()

    return render(request, 'cabriolets.html', {'cabriolets': cabriolets})


def catalog5(request):
    retro = models.Retro.objects.all()

    return render(request, 'retro.html', {'retro':retro })


def catalog6(request):
    transfer = models.Transfer.objects.all()

    return render(request, 'transfer.html', {'transfer': transfer    })