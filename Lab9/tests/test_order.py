from pages.checkout_page import CheckoutPage
import unittest
import json
from parameterized import parameterized
from config.config import TestData
import time

class TestOrder(unittest.TestCase):
    def setUp(self):
        with open(TestData.ORDER) as f:
            self._test_data = json.load(f)
        
        self._controller = CheckoutPage()
        self._controller.open_page(TestData.BASE_URL)

    def tearDown(self):
        self._controller.close()

    def _load_data_from_file(self, file_path, json_name):
        test_data = None
        with open(file_path) as f:
            test_data = json.load(f)
            test_data = test_data[json_name]
        return test_data

    def test_with_auth(self):
        item = self._load_data_from_file(TestData.AUTH_TEST_FILE_PATH, 'valid')
        time.sleep(5)
        self._controller.goto_login()
        self._controller.enter_username(item['login'])
        self._controller.enter_password(item['password'])
        self._controller.click_login()
        time.sleep(1)
        self._controller.open_page(TestData.BASE_URL)
        time.sleep(1)
        self._controller.add_to_cart_one_item()
        time.sleep(1)
        elem = self._controller.check_cart_item()
        self.assertEqual(elem.text, self._controller.FIRST_PRODUCT, msg='error with name product')

        self._controller.confirm_order()
        self._controller.confirm_checkout()
        err_msg = self._controller.check_error()
        self.assertEqual(err_msg, self._controller.ERROR_MESSAGE, msg='Error with redirect to error page')    

    def test_without_auth(self):  

        self._controller.add_to_cart_one_item()
        time.sleep(1)
        elem = self._controller.check_cart_item()
        self.assertEqual(elem.text, self._controller.FIRST_PRODUCT, msg='error with name product')

        test_data = self._load_data_from_file(TestData.ORDER, 'valid')
        self._controller.confirm_order()
        time.sleep(2)
        self._controller.fill_inputs(test_data)
        time.sleep(1)
        self._controller.confirm_checkout()

        err_msg = self._controller.check_error()
        self.assertEqual(err_msg, self._controller.ERROR_MESSAGE, msg='Error with redirect to error page')

    @parameterized.expand([
        ['busy_email'],
        ['busy_login']
    ])
    def test_without_auth_with_busy_parameters(self, name):
        test_data = self._test_data[name]
        time.sleep(5)
        self._controller.add_to_cart_one_item()
        time.sleep(1)
        elem = self._controller.check_cart_item()
        self.assertEqual(elem.text, self._controller.FIRST_PRODUCT, msg='error with name product')

        self._controller.confirm_order()
        time.sleep(2)

        self._controller.fill_inputs(test_data)
        self._controller.confirm_checkout()
        time.sleep(1)
        self.assertTrue(self._controller.check_availaility(self._controller.ALERT), msg=f'error with alert msg for {name}')