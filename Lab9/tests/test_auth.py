from pages.login_page import LoginPage
import unittest
import json
from parameterized import parameterized
from config.config import TestData

class TestAuth(unittest.TestCase):
    def setUp(self):
        with open(TestData.AUTH_TEST_FILE_PATH) as f:
            self._test_data = json.load(f)

        self._controller = LoginPage()
        self._controller.open_page(TestData.BASE_URL)
        self._controller.goto_login()

    def tearDown(self):
        self._controller.close()

    @parameterized.expand([
        ['valid',  'alert-success'],
        ['invalid', 'alert-danger']
    ])

    def test_auth(self, name, msg):
        item = self._test_data[name]
        self._controller.enter_username(item['login'])
        self._controller.enter_password(item['password'])

        self.assertTrue(self._controller.check_availaility('has-success'), msg='error with success icon')

        self._controller.click_login()

        self.assertTrue(self._controller.check_availaility(msg), msg=f'error with {msg}')

    def test_auth_with_empty_data(self):
        item = self._test_data['empty']
        self._controller.enter_username(item['login'])
        self._controller.enter_password(item['password'])

        self.assertTrue(self._controller.check_availaility('has-error'), msg='error with error icon')

        self._controller.click_login()

        self.assertFalse(self._controller.check_availaility('alert-success'), msg='error with alert')
        self.assertFalse(self._controller.check_availaility('alert-danger'), msg='error with alert')