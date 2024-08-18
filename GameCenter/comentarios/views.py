from django.shortcuts import render
from .models import comentarios
# Create your views here.
def blog(request):
    Comentarios=comentarios.objects.all()
    return render(request, "comentarios/blog.html", {'comentarios':Comentarios})