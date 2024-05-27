from .base_page import BasePage
from config.config import TestData
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = 'btn-default'
    CONFIRM_BUTTON = 'confirm'
    ACCOUNT = 'Account'
    ENTER = 'Вход'
    LOGIN_BUTTON = 'btn'
    LOGIN_INPUT = 'login'
    PASSWORD_INPUT = 'password'
    LOGIN_BUTTON = 'btn'
    FIRST_PRODUCT = '1234'
    BUTTON_ADD_TO_CART = 'ADD TO CART'
    XPATH_CART_ITEM1 ='//*[@id="cart"]/div/div/div[2]/div/table/tbody/tr[1]/td[2]/a'
    XPATH_ERROR = '/html/body/h1'
    ERROR_MESSAGE = 'Произошла ошибка'
    CONFIRM_BUTTON = 'btn-primary'
    LOGIN_STR = 'login'
    PASSWORD_STR = 'password'
    NAME_STR = 'name'
    EMAIL_STR = 'email'
    ADDRESS_STR = 'address'
    ALERT = 'alert-danger'

    def goto_login(self):
        self.click_on_hyperlink(self.ACCOUNT)
        self.click_on_hyperlink(self.ENTER)
    
    def click_login(self):
        self.click_on_button(self.LOGIN_BUTTON)
    
    def enter_username(self, username):
        self.enter_value_in_input(self.LOGIN_INPUT, username)

    def enter_password(self, password):
        self.enter_value_in_input(self.PASSWORD_INPUT, password)
   
    def add_to_cart_one_item(self):
        self.click_on_hyperlink(self.FIRST_PRODUCT)
        self.click_on_hyperlink(self.BUTTON_ADD_TO_CART)

    def check_cart_item(self):
        return self.find_elem_by_xpath(self.XPATH_CART_ITEM1)
    
    def confirm_order(self):
        self.click_on_button(self.CONFIRM_BUTTON)

    def confirm_checkout(self):
        self.click_on_button(self.CHECKOUT_BUTTON)

    def check_error(self):
        return self.find_elem_by_xpath(self.XPATH_ERROR).text  
    
    def fill_inputs(self, data):
        self.enter_value_in_input(self.LOGIN_STR, data['login'])
        self.enter_value_in_input(self.PASSWORD_STR, data['password'])
        self.enter_value_in_input(self.NAME_STR, data['name'])
        self.enter_value_in_input(self.EMAIL_STR, data['email'])
        self.enter_value_in_input(self.ADDRESS_STR, data['address'])
