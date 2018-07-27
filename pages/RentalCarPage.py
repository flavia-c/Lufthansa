from selenium.webdriver.common.by import By
from .MoreOptionsPage import MoreOptionsPage
from .Utils import Utils

class RentalCarPage:

    __SEARCH_CAR_BUTTON = (By.XPATH, '//div[@id="flightmanager-tabpanel-2"]//button')
    __MORE_OPTIONS_BUTTON = (By.LINK_TEXT, 'Search with more options')

    __PICKUP_ERROR_TEXT = (By.ID, 'flightmanagerCarFormpickup-location-name-msg')
    __PICKUP_DATE_ERROR_TEXT = (By.ID, 'flightmanagerCarFormpickupDateDisplay-msg')
    __DROPOFF_ERROR_TEXT = (By.ID, 'flightmanagerCarFormdropoff-location-name-msg')
    __DROPOFF_DATE_ERROR_TEXT = (By.ID, 'flightmanagerCarFormdropoffDateDisplay-msg')

    def __init__(self, driver):
        self.driver = driver

    def more_options(self):
        el = Utils.wait_for_element_to_be_clickable(self, self.driver, self.__MORE_OPTIONS_BUTTON)
        el.click()

        return MoreOptionsPage(self.driver)

    def click_submit(self, confirm_page):
        el = Utils.wait_for_element_to_be_clickable(self, self.driver, self.__SEARCH_CAR_BUTTON)
        el.click()

        return Utils.driver_redirector(self, self.driver, MoreOptionsPage, RentalCarPage, confirm_page)

    def get_pickup_location_error(self):

        return Utils.get_text_from_element(self, self.driver, self.__PICKUP_ERROR_TEXT)

    def get_pickup_date_error(self):

        return Utils.get_text_from_element(self, self.driver, self.__PICKUP_DATE_ERROR_TEXT)

    def get_dropoff_location_error(self):

        return Utils.get_text_from_element(self, self.driver, self.__DROPOFF_ERROR_TEXT)

    def get_dropoff_date_error(self):

        return Utils.get_text_from_element(self, self.driver, self.__DROPOFF_DATE_ERROR_TEXT)