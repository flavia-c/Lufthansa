from selenium import webdriver
import pytest

class BasePage:

    @pytest.fixture(autouse=True)
    def setup(self):

        self.driver = webdriver.Chrome('C:\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.lufthansa.com/online/portal/lh/ro/homepage')

        yield self.driver

        self.driver.close()
        self.driver.quit()