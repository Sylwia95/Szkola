from test_data.registration_data import  RegistrationDataGenerator
from tests.main_test import MainTest



class RegistrationTest(MainTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()
        self.main_page.click_register_button()
        self.register_page = self.main_page.click_register_button()

    def testcompleteform (self):
        self.register_page.enter_first_name(self.data.first_name)
        self.register_page.enter_last_name(self.data.last_name)
        self.register_page.enter_address(self.data.address)
        self.register_page.enter_city(self.data.city)
        self.register_page.enter_state("Mazowieckie")
        self.register_page.enter_zip_code(self.data.zip_code)
        self.register_page.enter_phone(self.data.phone)
        self.register_page.enter_pesel(self.data.pesel)
        self.register_page.enter_username(self.data.username)
        self.register_page.enter_password(self.data.password)
        self.register_page.enter_confirm_password(self.data.password)
        self.register_page.click_button_register()
