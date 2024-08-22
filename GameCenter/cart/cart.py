from productos.models import JuegosXbox
class Cart():
    def __init__(self, request):
        self.session = request.session
        
        #Obtener la llave de sesion si (if) existe
        cart = self.session.get('session_key')

        #Si el usuario es nuevo
        if 'session_key'not in request.session:
            cart =self.session['session_key'] = {}

        
        #Asegurarse de que el carrito este disponible en todas las páginas del sitio
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        #Logica
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.precio)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #Obtener los ids del carrito
        product_ids = self.cart.keys()
        #Usar los ids para buscar los productos en la base de datos del modelo
        products = JuegosXbox.objects.filter(id__in=product_ids)

        #Retornar los productos buscados
        return products
