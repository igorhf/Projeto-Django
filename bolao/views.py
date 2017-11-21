from django.shortcuts import render
from django.http import HttpResponse
from .models import Partida


def index(request):
    partidas = Partida.objects.all()
    contexto = {'partidas': partidas}
    return render(request, 'index.html', contexto)


def aposta(request):
    partidas = Partida.objects.all()
    contexto = {'partidas': partidas}
    return render(request, 'aposta.html', contexto)

