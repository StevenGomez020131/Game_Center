from django.shortcuts import render, HttpResponse

# Create your views here.
menu="""
    <a href="/">Home</a>
    <a href="/contacto">Contacto</a>
"""
def inicio(request):
    return render(request,"inicio/inicio.html")

def contacto(request):

    return render(request, "inicio/contacto.html")