from django.shortcuts import render, HttpResponse
from .forms import ContactoForm

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

def accesoriosGeneral(request):
    return render(request, "inicio/accesoriosGeneral.html")

def juegosGeneral(request):
    return render(request, "inicio/juegosGeneral.html")

def formulario(request):
    return render(request, "inicio/formulario.html")

#Recepción de los datos del contacto desde el fomrulario

def contactoForm(request):
    if request.method =='POST':
        form =ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'inicio/formulario.html')
    form = ContactoForm()
    return render(request,'inicio/formulario.html',{'form':form})



