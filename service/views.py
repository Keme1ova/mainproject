from django.shortcuts import render
from . import models

def service(request):
    dec = models.Offer.objects.all()
    

    return render(request, 'service.html', {'dec': dec})

