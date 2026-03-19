from base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    """
    First Page Locators
    """
    REGISTER_BUTTON = (By.ID, "Register")

class FirstPage(BasePage):
    """
    First Page Object
    """
    def  click_register_button(self):
        self.driver.find_element(*LOCATORS.REGISTER_BUTTON).click()
        return register_page

