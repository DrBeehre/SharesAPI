from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import traceback
import time

def get_sharesies_portfolio_value(email, password):
    driver = webdriver.Chrome("C:\\Users\Ward\Downloads\chromedriver_win32\chromedriver")

    portfolioValue = None

    try:
        driver.get("https://app.sharesies.nz/login")

        username_field = driver.find_element_by_name("email")
        username_field.send_keys(email)

        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(3)

        portfolioValues = driver.find_element_by_class_name("DiversitySegment__portfolioValue__2GTcj")
        portfolioValue = portfolioValues.text.splitlines()[0]
        
    except Exception as ex:
        traceback.print_exception()
        driver.quit()
    finally:
        driver.quit()
        return portfolioValue