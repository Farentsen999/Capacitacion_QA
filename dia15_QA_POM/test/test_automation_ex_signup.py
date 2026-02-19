import pytest
from playwright.sync_api import expect
from pages.automation_ex.signup_login_page import SignupLoginPage

def test_sign_up (page):
    # 1. Iniciamos en la pagina de login/signup
    signup = SignupLoginPage(page)
    signup.navegar()
    signup_details = signup.iniciar_registro("Luciano", "matias100075@gmail.com")
            
    # Datos necesarios para crear una nueva cuenta
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
    
    # 2. Creamos cuenta
    new_account = signup_details.create_acount(datos)
    
    # 3. Confirmamos la creación de la cuenta
    expect(new_account.account_created_confirmation).to_have_text("Account Created!")
    
    # 4. Vamos a la home
    home1 = new_account.continuar()
    
    # 5. Verificamos que home indique que nos logeamos con la cuenta creada
    expect(home1.logged_in_as).to_contain_text("Logged in as")
    
    # 6. Eliminamos la cuenta creada
    delete_account = home1.delete_account()
    
    # 7. Confirmamos la eliminación de la cuenta creada
    expect(delete_account.account_deleted_confirmation).to_have_text("Account Deleted!")
    
    # 8. Volvemos a home
    home2 = delete_account.continuar()
    
    # 9. Verificamos que estamos en home
    expect(home2.page).to_have_url("https://automationexercise.com/")