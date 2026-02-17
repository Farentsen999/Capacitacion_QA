# Desarrollo Parcial
class SignupDetailsPage:
    def __init__(self, page):
        self.page = page
        self.gender_male_locator = '#id_gender1'
        self.gender_female_locator = '#id_gender2'
        self.newsletter_locator = '#newsletter'
        self.optin_locator = '#optin'
        
        self.name_input = page.locator('[data-qa="name"]')
        self.password_input = page.locator('[data-qa="password"]')
        self.birth_day_input = page.locator('[data-qa="days"]')
        self.birth_month_input = page.locator('[data-qa="months"]')
        self.birth_year_input = page.locator('[data-qa="years"]')
        
        self.first_name_input = page.locator('[data-qa="first_name"]')
        self.last_name_input = page.locator('[data-qa="last_name"]')
        self.country_input = page.locator('[data-qa="country"]')
        self.company_input = page.locator('[data-qa="company"]')
        self.address1_input = page.locator('[data-qa="address"]')
        self.address2_input = page.locator('[data-qa="address2"]')
        self.state_input = page.locator('[data-qa="state"]')
        self.city_input = page.locator('[data-qa="city"]')
        self.zip_input = page.locator('[data-qa="zipcode"]')
        self.number_input = page.locator('[data-qa="mobile_number"]')
        self.create_acount_button = page.locator('[data-qa="create-account"]')
        
    def create_acount(self, data):
        if(data['gender'] == 'Male'): 
            self.page.check(self.gender_male_locator)
        else:
            self.page.check(self.gender_female_locator)
            
        self.name_input.fill(data['username'])
        self.password_input.fill(data['password'])
        self.birth_day_input.select_option(data['birth_date']['day'])
        self.birth_month_input.select_option(data['birth_date']['month'])
        self.birth_year_input.select_option(data['birth_date']['year'])
        self.page.check(self.newsletter_locator)
        self.page.check(self.optin_locator)
        self.first_name_input.fill(data['name'])
        self.last_name_input.fill(data['lastname'])
        self.country_input.select_option(data['country'])
        self.company_input.fill(data['company'])
        self.address1_input.fill(data['address1'])
        self.address2_input.fill(data['address2'])
        self.state_input.fill(data['state'])
        self.city_input.fill(data['city'])
        self.zip_input.fill(data['zipcode'])
        self.number_input.fill(data['mobile_number'])
        self.create_acount_button.click()
        self.page.wait_for_url("https://automationexercise.com/account_created")
        return self.page
        
        
        
        
        