import BasePgae from base_page
from selenium.webdriver.common.by import By

class Locators:
    """
    First Page Locators
    """
    REGISTER_BUTTON = (By.loginPanel, "Register")

class FirstPage(BasePgae):
    """
    First Page Object
    """
    def  click_register_button(self):
        self.driver.find_element(*LOCATORS.REGISTER_BUTTON).click()

