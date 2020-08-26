from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import traceback
import time

def get_hatch_portfolio_value(email, password):
    driver = webdriver.Chrome("C:\\Users\Ward\Downloads\chromedriver_win32\chromedriver")

    path = "https://app.hatchinvest.nz/"

    portfolio_value = None

    try:
        driver.get(path)
        time.sleep(1)

        username_field = driver.find_element_by_id("user_email")
        username_field.send_keys(email)

        password_field = driver.find_element_by_id("user_password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        
        time.sleep(2)

        currency_selecter = Select(driver.find_element_by_id("selectedPeriod"))
        currency_selecter.select_by_value("NZD")

        time.sleep(2)

        portfolio_value = driver.find_element_by_class_name("investment-value__section-content").text
        
    except Exception as ex:
        traceback.print_exception()
        driver.quit()
    finally:
        driver.quit()
        return portfolio_value

    