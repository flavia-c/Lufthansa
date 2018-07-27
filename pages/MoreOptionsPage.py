from selenium import webdriver
from selenium.webdriver.common.by import By
from .Utils import Utils

class MoreOptionsPage:

    __PICKUP_FIELD = (By.ID, 'carPickupLocationName')

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return Utils.get_page_title(self, self.driver, self.__PICKUP_FIELD)

