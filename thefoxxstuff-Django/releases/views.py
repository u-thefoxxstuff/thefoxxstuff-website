from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import Album


def releases(request):
    album = Album.objects.all()
    context = {
        'album': album,
        'title': 'Релизы'
    }
    return render (request, template_name='releases/index.html', context=context )

def album(request):
    print(request)
    return HttpResponse ('album')

