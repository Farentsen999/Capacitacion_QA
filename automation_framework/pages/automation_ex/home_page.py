class HomedPage:
    def __init__(self, page):
        self.page = page
        self.delete_account_button = page.locator("li:has(i.fa-trash-o)")
        self.logged_in_as = page.locator("li:has(i.fa-user)")

    def delete_account(self):
        self.delete_account_button.click()
        self.page.mouse.click(0, 0)
        self.page.wait_for_url("https://automationexercise.com/delete_account")
        from pages.automation_ex.account_deleted_page import AccountDeletedPage
        return AccountDeletedPage(self.page)
        
