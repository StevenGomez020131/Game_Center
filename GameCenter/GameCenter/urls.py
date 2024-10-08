"""
URL configuration for GameCenter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inicio import views
from django.conf import settings
from productos import views as views_productos
from comentarios import views as views_comentarios
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.inicio, name="Inicio"),
    path("contacto/",views.contacto, name="Contacto"),
    path("productos/",views.productos, name="Productos"),
    path("blog/", views_comentarios.blog, name="Blog"),
    path('carrito/', views_productos.carrito, name='Carrito'),
    path("accesoriosGeneral/", views.accesoriosGeneral, name="AccesoriosGeneral"),
    path("juegosGeneral/",views.juegosGeneral, name="JuegosGeneral"),
    path("formulario/", views.formulario, name= "Formulario" ),
    path("registrar/", views_comentarios.registrar, name="Registrar"),
    path("juegosxbox/", views_productos.JuegosXboxx, name="JuegosXbox"),
    path("contactoform/", views.contactoForm, name="RegistrarFormulario"),
    path("juegosplay/", views_productos.JuegosPlayStation, name="JuegosPlayStation"),
    path("juegosnintendo/", views_productos.JuegosNintendo, name="JuegosNintendo"),
    path("juegospc/", views_productos.JuegosPc, name="JuegosPC"),
    path("accesoriosxbox/", views_productos.AccesoriosXbox, name="AccesoriosXbox"),
    path("accesoriosplay/", views_productos.AccesoriosPlayStation, name="AccesoriosPlayStation"),
    path("accesoriosnintendo/", views_productos.AccesoriosNintendo, name="AccesoriosNintendo"),
    path("accesoriospc/", views_productos.AccesoriosPC, name="AccesoriosPC"),
    path("cart/", include("cart.urls")),





]
if settings.DEBUG:

    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
