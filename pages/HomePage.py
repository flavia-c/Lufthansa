from selenium.webdriver.common.by import By
from .Utils import Utils
from .RentalCarPage import RentalCarPage

class HomePage:

    __RENTAL_CAR_TAB = (By.ID, 'flightmanager-tab-2')

    def __init__(self, driver):
        self.driver = driver

    def select_rental_car(self):
        el = Utils.wait_for_element_to_be_clickable(self, self.driver, self.__RENTAL_CAR_TAB)
        el.click()

        return RentalCarPage(self.driver)





