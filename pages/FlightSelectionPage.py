from selenium.webdriver.common.by import By
from pages.Utils import Utils

class FlightSelectionPage:

    __CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button.nextBtn.mandatory')
    #__FLIGHT_RESULT_TABLE = (By.CSS_SELECTOR, 'div.ng-tns-c13-1')
    __FLIGHT_OPTIONS = ((By.CSS_SELECTOR, 'cont-avail.ng-tns-c13-1'))

    def __init__(self, driver):
        self.driver = driver
        Utils.wait_for_element_to_be_visible(self, self.driver, self.__CONTINUE_BUTTON)

    def get_results_page_title(self):
        #return Utils.get_page_title(self, self.driver, self.__CONTINUE_BUTTON)
        return self.driver.title

    def count_flight_options(self):
        #element = Utils.wait_for_element_to_be_visible(self, self.driver, self.__FLIGHT_RESULT_TABLE)
        options = Utils.wait_for_elements_to_be_visible(self, self.driver, self.__FLIGHT_OPTIONS)

        """for option in options:
            self.__MYLIST.append(option)"""

        return (len(options))




