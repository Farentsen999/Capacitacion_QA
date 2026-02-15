from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage

def test_flujo_completo_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context(
            record_video_dir="evidence/videos/",
            viewport={'width': 1280, 'height': 720}
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        
        try:
            # 1. Iniciamos en Login
            login = LoginPage(page)
            login.navegar()
            
            # 2. Validar que los elementos para el ingreso de datos esten habilitados
            expect(login.username_input).to_be_editable()
            expect(login.password_input).to_be_editable()
            
            # 3. El login me entrega el inventario automáticamente
            inventario = login.login("standard_user", "secret_sauce")
            
            # 4. Acciones en inventario
            productos = inventario.obtener_todos_los_productos()
            inventario.comprar_producto(productos)
            
            # 5. Ir al carrito
            carrito = inventario.ir_al_carrito()
            
            # 6. Validación en Carrito
            assert carrito.verificar_datos(productos) == False
            expect(page.locator(".shopping_cart_badge")).to_have_text(str(len(productos)))
            
            # 7. Ir a checkout
            checkout = carrito.ir_a_checkout()
            
            # 8. Validar que los elementos para el ingreso de datos esten habilitados
            expect(checkout.username_input).to_be_editable()
            expect(checkout.password_input).to_be_editable()
            expect(checkout.zip_code).to_be_editable()
            
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
                    
        except Exception as e:
            page.screenshot(path="evidence/screenshots/failed_test.png")
            raise e
        finally:
            context.tracing.stop(path="evidence/trace.zip")
            context.close()
            browser.close()

if __name__ == "__main__":
    test_flujo_completo_pom()