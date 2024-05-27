from .base_page import BasePage

class LoginPage(BasePage):
    LOGIN_INPUT = 'login'
    PASSWORD_INPUT = 'password'
    LOGIN_BUTTON = 'btn'
    ACCOUNT_LINK = 'Account'
    ENTER_LINK = 'Вход'

    def enter_username(self, username):
        self.enter_value_in_input(self.LOGIN_INPUT, username)

    def enter_password(self, password):
        self.enter_value_in_input(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_on_button(self.LOGIN_BUTTON)

    def goto_login(self):
        self.click_on_hyperlink(self.ACCOUNT_LINK)
        self.click_on_hyperlink(self.ENTER_LINK)

