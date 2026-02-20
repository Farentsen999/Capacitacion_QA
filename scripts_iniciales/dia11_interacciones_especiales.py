from playwright.sync_api import sync_playwright, expect
import time

def test_interacciones_especiales():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://automationexercise.com/contact_us")
        
        page.wait_for_selector('[data-qa="name"]')
        
        page.type('[data-qa="name"]', "Matias", delay=50)
        email_unico = f"test_qa_{int(time.time())}@gmail.com"
        page.type('[data-qa="email"]', email_unico, delay=50)
        page.type('[data-qa="subject"]', "Subir archivo para prueba curso QA", delay=50)
        page.type('[data-qa="message"]', "Voy a subir un archivo de prueba", delay=50)
        page.set_input_files('input[name="upload_file"]', "reporte_final.json")
        
        page.on("dialog", lambda dialog: dialog.accept())
        
        page.click('[data-qa="submit-button"]')
        
        mensaje_exito = page.locator(".status.alert.alert-success")
        expect(mensaje_exito).to_be_visible()
        
        print("¡Test de alertas y subida de archivos exitoso!")
        browser.close() 
    
if __name__ == "__main__":
    test_interacciones_especiales()