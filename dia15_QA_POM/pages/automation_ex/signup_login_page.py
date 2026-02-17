class SignupLoginPage:
    def __init__(self, page):
        self.page = page
        self.signup_name_input = page.locator('[data-qa="signup-name"]')
        self.signup_email_input = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')

    def navegar(self):
        self.page.goto("https://automationexercise.com/login")

    def iniciar_registro(self, nombre, email):
        self.signup_name_input.fill(nombre)
        self.signup_email_input.fill(email)
        self.signup_button.click()
        self.page.wait_for_url("**/signup**")
        from pages.automation_ex.signup_details_page import SignupDetailsPage
        return SignupDetailsPage(self.page)
        
        
        