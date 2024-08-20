from django.shortcuts import render, get_object_or_404
from .cart import Cart
from productos.models import accesoriosXbox
from productos.models import accesoriosPlayStation
from productos.models import accesoriosNintendo
from productos.models import accesoriosPC
from productos.models import JuegosXbox
from django.http import JsonResponse

def cart_summary(request):
    #Obtener el carrito
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "cart_summary.html", {"cart_products":cart_products})

def cart_add(request):
    #Obtener el carrito
    cart = Cart(request)

    #Probamos para el POST
    if request.POST.get('action') == 'post':

        #Obtener las cosas
        product_id =int(request.POST.get('product_id'))

        #Buscar el producto/accesorio en la DB
        product =get_object_or_404(JuegosXbox, id=product_id)

        #Para guardar la sesion
        cart.add(product=product)

        #Obtener la cantidad del carrito
        cart_quantity = cart.__len__()

        #Devolver la repuesta
        #response = JsonResponse({'Product Name: ': product.nombre})
        response = JsonResponse({'qty: ': cart_quantity})
        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass

