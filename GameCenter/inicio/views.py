from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"inicio/inicio.html")

def contacto(request):

    return render(request, "inicio/contacto.html")

def productos(request):

    return render(request, "inicio/productos.html")

def blog(request):

    return render(request, "inicio/blog.html")

def carrito(request):
    return render(request, "inicio/carrito.html")

