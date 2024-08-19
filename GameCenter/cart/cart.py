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