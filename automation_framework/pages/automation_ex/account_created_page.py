class AccountCreatedPage:
    def __init__(self, page):
        self.page = page
        self.continue_button = page.locator('[data-qa="continue-button"]')
        self.account_created_confirmation = page.locator('[data-qa="account-created"]')

    def continuar(self):
        self.continue_button.click()
        self.page.mouse.click(0, 0)
        self.page.wait_for_url("https://automationexercise.com")
        from pages.automation_ex.home_page import HomedPage
        return HomedPage(self.page)
        