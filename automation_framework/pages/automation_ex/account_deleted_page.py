class AccountDeletedPage:
    def __init__(self, page):
        self.page = page
        self.continue_button = page.locator('[data-qa="continue-button"]')
        self.account_deleted_confirmation = page.locator('[data-qa="account-deleted"]')

    def continuar(self):
        self.continue_button.click()
        self.page.wait_for_url("https://automationexercise.com")
        from pages.automation_ex.home_page import HomedPage
        return HomedPage(self.page)
        