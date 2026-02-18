from playwright.sync_api import sync_playwright, expect
from pages.automation_ex.signup_login_page import SignupLoginPage

def sign_up_test ():
    with sync_playwright() as p:            
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="evidence/videos/",
            viewport={'width': 1280, 'height': 720}
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
            
        try:
            signup = SignupLoginPage(page)
            signup.navegar()
            signup_details = signup.iniciar_registro("Luciano", "matias100075@gmail.com")
            
            datos = {
            'gender':"Male",
            'username':"Francisco",
            'password':"123456980",
            'birth_date': {'day': "6", 'month': "January", 'year': "1999"},
            'name':"Mateo",
            'lastname':"Aros",
            'country':"Canada",
            'company':"QA.inc",
            'address1':"Toronto",
            'address2':"Quebec",
            'state':"Canada",
            'city':"Toronto",
            'zipcode':"44001",
            'mobile_number':"977552595"            
            }
            new_account = signup_details.create_acount(datos)
            expect(new_account.account_created_confirmation).to_have_text("Account Created!")
            
            home1 = new_account.continuar()
            expect(home1.logged_in_as).to_contain_text("Logged in as")
            
            delete_account = home1.delete_account()
            expect(delete_account.account_deleted_confirmation).to_have_text("Account Deleted!")
            home2 = delete_account.continuar()
            expect(home2.page).to_have_url("https://automationexercise.com/")
    
        except Exception as e:
            page.screenshot(path="evidence/screenshots/failed_test.png")
            raise e
        
        finally:
            context.tracing.stop(path="evidence/trace_automation_ex_test_flow.zip")
            context.close()
            browser.close()


if __name__ == "__main__":
    sign_up_test()