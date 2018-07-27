from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import timedelta
from datetime import datetime
import pytest
from selenium.webdriver.support.select import Select
from pages.Utils import Utils
from pages.FlightSelectionPage import FlightSelectionPage

class FlightsPage:
    __ORIGIN_FIELD = (By.NAME, 'originName1')
    __DESTINATION_FIELD = (By.NAME, 'destinationName1')

    """__ORIGIN_BUTTON = (By.ID, 'flightmanagerFlightsFormAirportAtlasOrigin')
    __DESTINATION_BUTTON = (By.ID, 'flightmanagerFlightsFormAirportAtlasDestination')

    __COUNTRY_DROPDOWN_ORIGIN = (By.ID, 'flightmanagerFlightsFormOriginAirportAtlasCountry')
    __CITY_DROPDOWN_ORIGIN = (By.ID, 'flightmanagerFlightsFormOriginAirportAtlasCity')
    __AIRPORT_DROPDOWN_ORIGIN = (By.ID, 'flightmanagerFlightsFormOriginAirportAtlasAirport')
    __SELECT_BUTTON = (By.XPATH, '//div[@class="modal-footer lid"]/input')

    __COUNTRY_DROPDOWN_DESTINATION = (By.ID, 'flightmanagerFlightsFormDestinationAirportAtlasCountry')
    __CITY_DROPDOWN_DESTINATION = (By.ID, 'flightmanagerFlightsFormDestinationAirportAtlasCity')"""

    __ONE_WAY_CHECKBOX = (By.XPATH, "//span[text()='One-way']")
    __DATE_PICKER = (By.ID, 'flightmanagerFlightsFormOutboundDateDisplay')

    __departing_date = datetime.today().date() + timedelta(days=14)
    __DEPARTING_DATE_SELECTOR = (By.XPATH, "//td[@data-kosa-calendar-date='" + str(__departing_date) + "']")
    __SEARCH_FLIGHTS_BUTTON = (By.XPATH, "//div[2]/div[2]/button[text()='Search flights']")


    def __init__(self, driver):
        self.driver = driver

    """def select_origin_flight_from_dropdown(self, country, city, airport):
        el = Utils.wait_for_element_to_be_clickable(self, self.driver, self.__ORIGIN_BUTTON)
        el.click()

        country_list_origin = Utils.wait_for_text_to_appear(self, self.driver, self.__COUNTRY_DROPDOWN_ORIGIN, country)
        country_option = Select(country_list_origin)
        country_option.select_by_visible_text(country)

        city_list_origin = Utils.wait_for_text_to_appear(self, self.driver, self.__CITY_DROPDOWN_ORIGIN, city)
        city_option = Select(city_list_origin)
        city_option.select_by_visible_text(city)

        airport_list_origin = Utils.wait_for_text_to_appear(self, self.driver, self.__AIRPORT_DROPDOWN_ORIGIN, airport)
        airport_option = Select(airport_list_origin)
        airport_option.select_by_visible_text(airport)

        #submit = Utils.wait_for_element_to_be_visible(self, self.driver, self.__SELECT_BUTTON)
        #submit.click()"""

    def select_origin_flight_by_input(self, airport_name):
        el = Utils.wait_for_element_to_be_visible(self, self.driver, self.__ORIGIN_FIELD)
        el.clear()
        el.send_keys(airport_name)

    def select_destination_flight_by_input(self, airport_name):
        el = Utils.wait_for_element_to_be_visible(self, self.driver, self.__DESTINATION_FIELD)
        el.clear()
        el.send_keys(airport_name)

    def one_way_option(self):
        el = Utils.wait_for_element_to_be_visible(self, self.driver, self.__ONE_WAY_CHECKBOX)
        el.click()

    def select_date(self):

        date_widget = Utils.wait_for_element_to_be_visible(self, self.driver, self.__DATE_PICKER)
        date_widget.click()

        set_date = Utils.wait_for_element_to_be_visible(self, self.driver, self.__DEPARTING_DATE_SELECTOR)
        set_date.click()

        print('Data selectata este: ', self.__departing_date)

    def search_flights(self, confirm_page):
        search_button = Utils.wait_for_element_to_be_visible(self, self.driver, self.__SEARCH_FLIGHTS_BUTTON)
        search_button.click()

        return Utils.driver_redirector(self, self.driver, FlightSelectionPage(self.driver), FlightsPage(self.driver), confirm_page)

















