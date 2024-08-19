from .cart import Cart

#Crear context processor (Procesador de contexto) para que nuestro carrito funcione en todas las páginas del sitio
def cart(request):
    #Retornar los datos por default en nuestro carrito
    return {'cart':Cart(request)}