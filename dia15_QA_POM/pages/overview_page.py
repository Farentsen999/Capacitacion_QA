import re

class OverviewPage:
    def __init__(self, page):
        self.page = page
        self.item_cards = page.locator(".cart_item")
        self.subtotal_price = page.locator(".summary_subtotal_label")
        self.finish_button = page.locator("#finish")
    
    def obtener_todos_los_productos(self):
        items = self.item_cards.all()
        lista = []
        for item in items:
            lista.append({
                "nombre": item.locator(".inventory_item_name").inner_text(),
                "precio": float(item.locator(".inventory_item_price").inner_text().replace('$', '')),
                "boton": item.locator("button")
            })
        return lista
    
    def verificar_datos(self,lista_productos):
        error = False
        lista_overview = self.obtener_todos_los_productos()
        if len(lista_productos) == len(lista_overview):
            for i in range(len(lista_productos)):
                if(lista_productos[i]['nombre'] != lista_overview[i]['nombre']) and (lista_productos[i]['precio'] != lista_overview[i]['precio']):
                    error = True
        else:
            error = True
        return error
    
    def comparar_suma_y_total(self):
        lista_overview = self.obtener_todos_los_productos()
        match = True
        total_esperado = sum(item['precio'] for item in lista_overview)
        if(float(re.findall(r'[0-9.]+', self.subtotal_price.inner_text())[0])) != total_esperado:
            match = False
        return match
        

    def pagina_final(self):
        self.finish_button.click()
        from.finish_page import FinishPage
        return FinishPage(self.page)
    