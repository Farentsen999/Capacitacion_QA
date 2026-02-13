from playwright.sync_api import sync_playwright, expect
import json
import re

def guardar_resultados(nombre_lista):
        try:
            with open('reporte_de_auditoria.json', 'w', encoding='utf-8') as archivo:
                json.dump(nombre_lista, archivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

def proyecto_final_semana2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. LOGIN
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # 2. LÓGICA DE SELECCIÓN (El cerebro del bot)
        items = page.locator(".inventory_item").all()
        lista_productos = []

        for item in items:
            nombre = item.locator(".inventory_item_name").inner_text()
            precio_raw = item.locator(".inventory_item_price").inner_text()
            precio_float = float(precio_raw.replace('$', ''))
            
            lista_productos.append({
                "nombre": nombre,
                "precio": precio_float,
            })
            item.locator("button").click()

        # 3. ENCONTRAR MÁXIMO Y MÍNIMO
        producto_caro = max(lista_productos, key=lambda x: x['precio'])
        producto_barato = min(lista_productos, key=lambda x: x['precio'])
        
        # 5. CHECKOUT Y VALIDACIÓN
        page.click(".shopping_cart_link")
        cantidad_items = int(page.locator('[data-test="shopping-cart-badge"]').inner_text())
        assert(cantidad_items) == len(lista_productos)
        
        items_carrito = page.locator(".cart_item").all()
        lista_productos_carrito = []  
        
        for item_carrito in items_carrito:
            nombre = item_carrito.locator(".inventory_item_name").inner_text()
            precio_raw = item_carrito.locator(".inventory_item_price").inner_text()
            precio_float = float(precio_raw.replace('$', ''))
            
            lista_productos_carrito.append({
                "nombre": nombre,
                "precio": precio_float,
            })
            
        assert(len(lista_productos_carrito)) == len(lista_productos)
        
        for i in range (len(lista_productos_carrito)):
            assert(lista_productos_carrito[i]['nombre']) == lista_productos[i]['nombre']
    
        page.click("#checkout")
        page.fill("#first-name", "Matias")
        page.fill("#last-name", "QA")
        page.fill("#postal-code", "12345")
        page.click("#continue")

        # 6. AUDITORÍA DE TOTALES
        total_esperado = sum(item['precio'] for item in lista_productos_carrito)
        assert(float(re.findall(r'[0-9.]+', page.locator(".summary_subtotal_label").inner_text())[0])) == total_esperado
        
        page.click("#finish")

        # 7. REPORTE FINAL
        lista_productos_carrito.append({"total_esperado" : total_esperado})
        guardar_resultados(lista_productos_carrito)
        
        expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
        
        browser.close()

if __name__ == "__main__":
    proyecto_final_semana2()