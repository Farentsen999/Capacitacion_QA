from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage

def test_flujo_completo_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 1. Iniciamos en Login
        login = LoginPage(page)
        login.navegar()
        
        # 2. El login me entrega el inventario automáticamente
        inventario = login.login("standard_user", "secret_sauce")
        
        # 3. Acciones en inventario
        productos = inventario.obtener_todos_los_productos()
        inventario.comprar_producto(productos)
        
        # 4. Ir al carrito (me entrega la página CartPage)
        carrito = inventario.ir_al_carrito()
        
        # 5. Validación en Carrito
        assert carrito.verificar_datos(productos) == False
        
        # 6. Ir a checkout
        checkout = carrito.ir_a_checkout()
        
        # 7. Ir a overview
        overview = checkout.continuar("Alfredo","123456789","11780")
        
        # 8. Validación en Overview
        assert overview.verificar_datos(productos) == False
        assert overview.comparar_suma_y_total() == True
        
        # Ir a la pagina final
        finish = overview.pagina_final()
        expect(finish.succes_message).to_have_text("Thank you for your order!")
        
        # Volver a inventario
        inventario2 = finish.retornar_a_productos()
        expect(inventario2.page).to_have_url("https://www.saucedemo.com/inventory.html")
                
        # Cerrar Navegador
        browser.close()

if __name__ == "__main__":
    test_flujo_completo_pom()