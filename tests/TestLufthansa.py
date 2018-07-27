import pytest
from pages.HomePage import HomePage
from pages.FlightsPage import FlightsPage
from pages.BasePage import BasePage
from pages.FlightSelectionPage import FlightSelectionPage

@pytest.mark.usefixtures('setup')
class TestRentalCar(BasePage):

    __PICKUP_LOCATION_ERROR = "Please enter your pickup location."
    __PICKUP_DATE_ERROR = "Please enter your pickup date."
    __DROPOFF_LOCATION_ERROR = "Please enter your drop off location."
    __DROPOFF_DATE_ERROR = "Please enter your drop off date."

    __MORE_OPTIONS_TITLE = "Booking - Lufthansa ® Romania"
    __FLIGHT_OPTIONS_TITLE = "Flight Selection"

    def test_blank_fields(self, setup):
        home_page = HomePage(setup)
        car_page = home_page.select_rental_car()
        car_page.click_submit(False)

        assert car_page.get_pickup_location_error() == self.__PICKUP_LOCATION_ERROR
        assert car_page.get_pickup_date_error() == self.__PICKUP_DATE_ERROR
        assert car_page.get_dropoff_location_error() == self.__DROPOFF_LOCATION_ERROR
        assert car_page.get_dropoff_date_error() == self.__DROPOFF_DATE_ERROR

    def test_more_options(self, setup):
        home_page = HomePage(setup)
        car_page = home_page.select_rental_car()
        more_options = car_page.more_options()

        assert more_options.get_page_title() == self.__MORE_OPTIONS_TITLE

    def test_flight_results_page(self, setup):
        flight = FlightsPage(setup)
        origin = flight.select_origin_flight_by_input('Munich')

        destination = flight.select_destination_flight_by_input('Sibiu International')
        one_way = flight.one_way_option()
        departing_date = flight.select_date()
        results_page = flight.search_flights(True)

        assert results_page.get_results_page_title() == self.__FLIGHT_OPTIONS_TITLE

    def test_nr_of_flights(self, setup):
        flight = FlightsPage(setup)
        origin = flight.select_origin_flight_by_input('Munich')

        destination = flight.select_destination_flight_by_input('Sibiu International')
        one_way = flight.one_way_option()
        departing_date = flight.select_date()
        results_page = flight.search_flights(True)
        nr_of_flights = results_page.count_flight_options()

        print("Nr de zboruri disponibile: " + str(nr_of_flights))
