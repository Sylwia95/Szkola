from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators:

    """
    Register Page Locators
    """
    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP_CODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    PESEL = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input[value='Register']")


class RegisterPage(BasePage):
    """
    Create Register Page Object
    """

    def enter_first_name (self, firstname):
        """
        Enter First Name

        """
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(firstname)

    def enter_last_name(self, lastname):
        """
        Enter Last Name

        """
        self.driver.find_element(*Locators.LastName).send_keys(lastname)

    def enter_address(self, address):
        """
        Enter Address

        """
        self.driver.find_element(*Locators.Address).send_keys(address)

    def enter_city(self, city):
        """
        Enter City

        """
        self.driver.find_element(*Locators.CITY).send_keys(city)

    def enter_state(self, state):
        """
        Enter State
        """
        self.driver.find_element(*Locators.STATE).send_keys(state)

    def enter_zip_code(self, zipcode):
        """
        Enter Zip Code
        """
        self.driver.find_element(*Locators.ZIP_CODE).send_keys(zipcode)

    def enter_phone(self, phone):
        """
        Enter Phone Number
        """
        self.driver.find_element(*Locators.PHONE).send_keys(phone)

    def enter_pesel(self, pesel):
        """
        Enter Pesel

        """
        self.driver.find_element(*Locators.PESEL).send_keys(pesel)

    def enter_username(self, username):
        """
        Enter Username

        """

        self.driver.find_element(*Locators.USERNAME).send_keys(username)

    def enter_password(self, password):
        """
        Enter Password

        """
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        """
        Enter Confirm Password

        """
    def click_button_register(self):
        """
        Click Button Register

        """
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
