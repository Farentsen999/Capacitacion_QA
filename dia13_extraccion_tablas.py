from playwright.sync_api import sync_playwright, expect

def test_extraccion_tabla():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/challenging_dom")
        
        datos_columna = []
        
        filas = page.locator("table tbody tr").all()
        for fila in filas:
            texto = fila.locator("td").nth(0).inner_text()
            datos_columna.append(texto)
        
        assert(len(datos_columna)) == 10
        print(f"¡Test de extracción de datos de tablas superado, el elemento 1 de la cuarta fila es {datos_columna[3]}!")
        browser.close()
    
if __name__ == "__main__":
    test_extraccion_tabla()