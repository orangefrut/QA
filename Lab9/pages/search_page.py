from .base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    SEARCH_CATEGORY = 'Men'
    XPATH_CATEGORY = '/html/body/div[4]/div[2]/div/div/ol/li[2]/a'
    FIND_INPUT_NAME = 's'
    FIND_INPUT_VALUE = 'часы2'

    def click_on_category(self):
        self.click_on_hyperlink(self.SEARCH_CATEGORY)

    def get_category_correctly(self):
        return self.find_elem_by_xpath(self.XPATH_CATEGORY)

    def search_valid(self):
        self.enter_value_in_input_with_enter(self.FIND_INPUT_NAME, self.FIND_INPUT_VALUE)

    def search_invalid(self):
        self.enter_value_in_input_with_enter(self.FIND_INPUT_NAME, '')
