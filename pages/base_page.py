class BasePage:
    """
    Base Page Object for each page
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()class BasePage: