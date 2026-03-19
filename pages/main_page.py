from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.register_page import RegisterPage

class Locators:
    """
    First Page Locators
    """
    REGISTER_BUTTON = (By.LINK_TEXT, "Register")

class MainPage(BasePage):
    """
    First Page Object
    """
    def  click_register_button(self):
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
        return RegisterPage(self.driver)

