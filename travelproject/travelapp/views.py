from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Profile


def demo(request):
    obj = Place.objects.all()
    det = Profile.objects.all()
    return render(request, "index.html", {'result': obj, 'run': det})

