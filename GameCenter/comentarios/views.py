from django.shortcuts import render
from .models import comentarios
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
# Create your views here.
def blog(request):
    Comentario=ComentarioContacto.objects.all()
    return render(request, "comentarios/blog.html", {'consultas':Comentario})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            Comentario=ComentarioContacto.objects.all()
            return render (request, 'comentarios/blog.html', {'consultas':Comentario})

    form = ComentarioContactoForm()
#Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'comentarios/blog.html',{'form': form})

