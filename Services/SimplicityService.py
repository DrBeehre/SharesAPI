from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import traceback

def get_simplicity_portfolio_value(email, password):

    driver = webdriver.Chrome("C:\\Users\Ward\Downloads\chromedriver_win32\chromedriver")

    path = "https://app.simplicity.kiwi/login"

    portfolio_values = []

    try:
        
        driver.get(path)

        user_name_field = driver.find_element_by_id("email")
        user_name_field.send_keys(email)

        password_field = driver.find_element_by_id("password")
        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)

        time.sleep(3)

        kiwisaver = None
        mortgage = None 

        head6s = driver.find_elements_by_tag_name('h6')

        kiwisaver_elements = []
        kiwisaver_elements.append(head6s[1].text)
        kiwisaver_elements.append(head6s[2].text)

        kiwisaver = ''.join(kiwisaver_elements)

        mortgage_elements = []
        mortgage_elements.append(head6s[4].text)
        mortgage_elements.append(head6s[5].text)

        mortgage = ''.join(mortgage_elements)

        portfolio_values.insert(kiwisaver)
        portfolio_values.insert(mortgage)

    except Exception as ex:
        traceback.print_exception()
        driver.quit()
    finally:
        driver.quit()
        return portfolio_values