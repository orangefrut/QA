from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:

    def __init__(self):
        self._driver = webdriver.Chrome()   

    def open_page(self, url):
        self._driver.get(url)

    def enter_value_in_input(self, input_name, value):
        elem = self._driver.find_element(By.NAME, input_name)
        elem.send_keys(value)

    def click_on_button(self, button_class_name):
        elem = self._driver.find_element(By.CLASS_NAME, button_class_name)
        elem.click()
        time.sleep(1)

    def click_on_hyperlink(self, hyperlink_text):
        elem = self._driver.find_element(By.LINK_TEXT, hyperlink_text)
        elem.click()
        time.sleep(1)

    def enter_value_in_input_with_enter(self, input_name, value):
        elem = self._driver.find_element(By.NAME, input_name)
        elem.send_keys(value)
        elem.send_keys(Keys.RETURN)

    def find_elem_by_xpath(self, xpath):
        return self._driver.find_element(By.XPATH, xpath)

    def check_availaility(self, elem_class_name):
        try:
            elem = self._driver.find_element(By.CLASS_NAME, elem_class_name)
            return True
        except:
            return False
        
    def close(self):
        self._driver.close()