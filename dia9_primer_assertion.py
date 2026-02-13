from playwright.sync_api import sync_playwright, expect

def test_validador_libros():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://books.toscrape.com")
        
        # CORRECCIÓN 1: Usar expect para validar el título
        expect(page).to_have_title("All products | Books to Scrape - Sandbox")

        # CORRECCIÓN 2: Selector CSS real para el primer libro
        page.locator("h3 a").first.click()

        # CORRECCIÓN 3: Método inner_text() y clase correcta
        # Esperamos a que el precio sea visible antes de leerlo
        precio_elemento = page.locator(".price_color")
        precio_texto = precio_elemento.inner_text() 
        
        precio_num = float(precio_texto.replace('£', ''))
        
        if precio_num < 10:
            print(f"ALERTA: El precio {precio_num} es menor a £10")
        else:
            print(f"Validación de precio exitosa: £{precio_num}")
        
        # VALIDACIÓN 3: Stock
        expect(page.locator(".instock.availability")).to_contain_text("In stock")

        print("Test completado con éxito.")
        browser.close()

if __name__ == "__main__":
    test_validador_libros()