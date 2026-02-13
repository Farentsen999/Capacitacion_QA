from playwright.sync_api import sync_playwright, expect
import time

def test_formulario_registro():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://automationexercise.com/login")
        
        page.wait_for_selector('[data-qa="signup-name"]')
        
        page.type('[data-qa="signup-name"]', "Matias", delay=50)
        email_unico = f"test_qa_{int(time.time())}@gmail.com"
        page.type('[data-qa="signup-email"]', email_unico, delay=50)
        page.click('[data-qa="signup-button"]')     
        
        page.wait_for_selector("#id_gender1") 
        
        page.check('#id_gender1')
        page.type('[data-qa="password"]', "pasword", delay=50)
        
        page.select_option('[data-qa="days"]', '1')
        page.select_option('[data-qa="months"]', 'January')
        page.select_option('[data-qa="years"]', '1999')
        
        page.check('#newsletter')
        page.check('#optin')
        
        page.type('[data-qa="first_name"]', "Matias", delay=50)
        page.type('[data-qa="last_name"]', "Aros", delay=50)
        page.type('[data-qa="company"]', "QA.inc", delay=50)
        page.type('[data-qa="address"]', "Toronto", delay=50)
        page.type('[data-qa="address2"]', "Quebec", delay=50)
        page.select_option('[data-qa="country"]', 'Canada')
        page.type('[data-qa="state"]', "Canada", delay=50)
        page.type('[data-qa="city"]', "Toronto", delay=50)
        page.type('[data-qa="zipcode"]', "44544", delay=50)
        page.type('[data-qa="mobile_number"]', "123456789", delay=50)
        
        page.click('[data-qa="create-account"]')
        
        expect(page.locator('[data-qa="account-created"]')).to_be_visible()
        
        print(f"¡Éxito! Cuenta creada para: {email_unico}")
        page.wait_for_timeout(3000)
        browser.close()   

if __name__ == "__main__":
    test_formulario_registro()