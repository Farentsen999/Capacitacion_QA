class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.item_cards = page.locator(".inventory_item")
        self.cart_icon = page.locator(".shopping_cart_link")

    def obtener_todos_los_productos(self):
        self.item_cards.first.wait_for(state="visible", timeout=5000)
        items = self.item_cards.all()
        lista = []
        for item in items:
            lista.append({
                "nombre": item.locator(".inventory_item_name").inner_text(),
                "precio": float(item.locator(".inventory_item_price").inner_text().replace('$', '')),
                "boton": item.locator("button")
            })
        return lista
    
    def comprar_producto(self,lista_productos):
        for item in lista_productos:
            item["boton"].click()
        

    def ir_al_carrito(self):
        self.cart_icon.click()
        self.page.wait_for_url("https://www.saucedemo.com/cart.html")
        from pages.saucedemo.cart_page import CartPage
        return CartPage(self.page)