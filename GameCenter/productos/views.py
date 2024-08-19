from django.shortcuts import render
from .models import JuegosXbox
from .models import accesoriosXbox
from .models import accesoriosPlayStation
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
    accesorios = accesoriosXbox.objects.all()
    return render (request,"productos/AccesoriosNintendo.html", {'accesorios' : accesorios})

def AccesoriosPC(request):
    accesorios = accesoriosXbox.objects.all()
    return render (request,"productos/AccesoriosPc.html", {'accesorios' : accesorios})

