from django.shortcuts import render, redirect, get_object_or_404
import json
from django.http import JsonResponse
from .models import JuegosXbox
from .models import accesoriosXbox
from .models import accesoriosPlayStation
from .models import accesoriosNintendo
from .models import accesoriosPC



# Create your views here.

def JuegosXboxx(request):
    juegos = JuegosXbox.objects.all()
    return render (request,"productos/JuegosXbox.html", {'juegos' : juegos})

def JuegosPlayStation(request):
    juegos = JuegosXbox.objects.all()
    return render (request,"productos/JuegosPlayStation.html", {'juegos' : juegos})

def JuegosNintendo(request):
    juegos = JuegosXbox.objects.all()
    return render (request,"productos/JuegosNintendo.html", {'juegos' : juegos})

def JuegosPc(request):
    juegos = JuegosXbox.objects.all()
    return render (request,"productos/JuegosPc.html", {'juegos' : juegos})

def AccesoriosXbox(request):
    accesorios = accesoriosXbox.objects.all()
    return render (request,"productos/AccesoriosXbox.html", {'accesorios' : accesorios})

def AccesoriosPlayStation(request):
    accesoriosPlay = accesoriosPlayStation.objects.all()
    return render (request,"productos/AccesoriosPlayStation.html", {'accesoriosPlay' : accesoriosPlay})

def AccesoriosNintendo(request):
    accesorioNintendo = accesoriosNintendo.objects.all()
    return render (request,"productos/AccesoriosNintendo.html", {'accesoriosNintendo' : accesorioNintendo})

def AccesoriosPC(request):
    accesoriosPc = accesoriosPC.objects.all()
    return render (request,"productos/AccesoriosPc.html", {'accesoriosPC' : accesoriosPc})

def carrito(request):
    return render(request, 'productos/carrito.html')












