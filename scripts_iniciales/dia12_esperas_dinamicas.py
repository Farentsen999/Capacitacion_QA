from playwright.sync_api import sync_playwright, expect

def test_esperas_dinamicas():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://the-internet.herokuapp.com/dynamic_loading/1")
        
        page.click('button')
        
        page.wait_for_selector("#finish h4")
        
        mensaje_exito = page.locator("#finish h4")
        expect(mensaje_exito).to_be_visible()
        
        print("¡Test completado superando la carga dinámica!")
        browser.close()
    
if __name__ == "__main__":
    test_esperas_dinamicas()