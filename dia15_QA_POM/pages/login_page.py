class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def navegar(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, usuario, password):
        self.username_input.fill(usuario)
        self.password_input.fill(password)
        self.login_button.click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.page)