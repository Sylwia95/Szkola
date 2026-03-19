import unittest
from selenium import webdriver
from pages.main_page import MainPage

class MainTest(unittest.TestCase):
    """
    Main Test for each Test Case
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        self.driver.quit()