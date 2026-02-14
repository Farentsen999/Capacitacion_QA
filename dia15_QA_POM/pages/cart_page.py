class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.shopping_button = page.locator("#continue_shopping")
        self.item_cards = page.locator(".cart_item")
    
    def obtener_todos_los_productos(self):
        items = self.item_cards.all()
        lista = []
        for item in items:
            lista.append({
                "nombre": item.locator(".inventory_item_name").inner_text(),
                "precio": float(item.locator(".inventory_item_price").inner_text().replace('$', '')),
            })
        return lista
        
    def verificar_datos(self,lista_productos):
        error = False
        lista_carrito = self.obtener_todos_los_productos()
        if len(lista_productos) == len(lista_carrito):
            for i in range(len(lista_productos)):
                if(lista_productos[i]['nombre'] != lista_carrito[i]['nombre']) and (lista_productos[i]['precio'] != lista_carrito[i]['precio']):
                    error = True
        else:
            error = True
        return error
    
    def ir_a_checkout(self):
        self.checkout_button.click()
        self.page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.page)
        
        