class FinishPage:
    def __init__(self, page):
        self.page = page
        self.succes_message = page.locator(".complete-header")
        self.inventory_button = page.locator("#back-to-products")
        
    def retornar_mensaje(self):
        return self.succes_message.inner_text()
        
    def retornar_a_productos(self):
        self.inventory_button.click()
        self.page.wait_for_url("https://www.saucedemo.com/inventory.html")
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.page)