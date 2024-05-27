from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    FIRST_PRODUCT = 'CITIZEN AT0696-59E'
    SECOND_PRODUCT = 'TEST PRODUCT'
    BUTTON_ADD_TO_CART = 'ADD TO CART'
    XPATH_CART_ITEM1 ='//*[@id="cart"]/div/div/div[2]/div/table/tbody/tr[1]/td[2]/a'
    XPATH_CART_ITEM2 ='//*[@id="cart"]/div/div/div[2]/div/table/tbody/tr[2]/td[2]/a'

    def add_to_cart_one_item(self):
        self.click_on_hyperlink(self.FIRST_PRODUCT)
        self.click_on_hyperlink(self.BUTTON_ADD_TO_CART)
    
    def add_to_cart_two_item(self):
        self.click_on_hyperlink(self.SECOND_PRODUCT)
        self.click_on_hyperlink(self.BUTTON_ADD_TO_CART)

    def check_cart_item(self):
        return self.find_elem_by_xpath(self.XPATH_CART_ITEM1)
    
    def check_cart_items(self):
        a = self.find_elem_by_xpath(self.XPATH_CART_ITEM1)
        b = self.find_elem_by_xpath(self.XPATH_CART_ITEM2)
        return [a, b]


