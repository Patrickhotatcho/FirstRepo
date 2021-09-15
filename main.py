from locater import MainPageLocators
import unittest
from unittest.main import main
from selenium import webdriver
import page

class pythonSearch(unittest.TestCase):
    
    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("c:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://hk.finance.yahoo.com/")
    def test(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = 'TSLA'
        mainPage.click_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
    
    def tearDown(self):
        self.driver.close()
    

if __name__ == "__main__":
    unittest.main();