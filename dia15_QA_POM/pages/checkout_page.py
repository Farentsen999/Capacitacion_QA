class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#first-name")
        self.password_input = page.locator("#last-name")
        self.zip_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")

    def continuar(self, usuario, contraseña, zip):
        self.username_input.fill(usuario)
        self.password_input.fill(contraseña)
        self.zip_code.fill(zip)
        self.continue_button.click()
        from pages.overview_page import OverviewPage
        return OverviewPage(self.page)
        
        
        
        