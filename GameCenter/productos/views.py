from django.shortcuts import render
from .models import JuegosXbox
# Create your views here.

def JuegosXboxx(request):
    juegos = JuegosXbox.objects.all()
    return render (request,"productos/JuegosXbox.html", {'juegos' : juegos})
