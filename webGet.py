from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

PATH = "c:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://hk.finance.yahoo.com/most-active")



table = WebDriverWait(driver,10).until(ec.presence_of_all_elements_located((By.ID,"scr-res-table")))




driver.quit()





