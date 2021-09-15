from logging import BASIC_FORMAT
from locater import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "yfin-usr-qry"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()
    def click_button(self):
        element = self.driver.find_element(*MainPageLocators.button)
        element.click()

class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No result found." not in self.driver.page_source