from playwright.sync_api import sync_playwright

def ejecutar_test_humano():
    with sync_playwright() as p:
        # Lanzamos con un canal específico (chrome) para ser más realistas
        browser = p.chromium.launch(headless=False)
        
        # Creamos un contexto con un "User Agent" de una persona normal
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        print("Navegando a DuckDuckGo (es más amigable para practicar que Google)...")
        # Tip de QA: Para aprender, usa buscadores menos agresivos con los bots
        page.goto("https://duckduckgo.com")

        # Buscamos el cuadro de texto (en DuckDuckGo el ID suele ser 'search_form_input_homepage')
        # O podemos usar un selector por placeholder
        selector_busqueda = "input[name='q']"
        
        page.wait_for_selector(selector_busqueda)
        page.type(selector_busqueda, "Playwright Python", delay=100) # delay simula tipeo humano
        page.press(selector_busqueda, "Enter")

        # Esperamos a que carguen los resultados
        page.wait_for_load_state("networkidle")
        
        page.screenshot(path="resultado_busqueda_dia_8.png")
        print("¡Logrado! Screenshot guardado.")
        
        browser.close()

if __name__ == "__main__":
    ejecutar_test_humano()