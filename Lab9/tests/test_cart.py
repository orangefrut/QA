from pages.cart_page import CartPage
import unittest
import json
from parameterized import parameterized
from config.config import TestData
import time

class TestCart(unittest.TestCase):
    def setUp(self):        
        self._controller = CartPage()
        self._controller.open_page(TestData.BASE_URL)

    def tearDown(self):
        self._controller.close()

    def test_add_one_product(self):
        self._controller.add_to_cart_one_item()
        time.sleep(2)
        elem = self._controller.check_cart_item()
        self.assertTrue(elem.text, self._controller.FIRST_PRODUCT)

    def test_add_products(self):
        self._controller.add_to_cart_one_item()
        self._controller.open_page(TestData.BASE_URL)
        self._controller.add_to_cart_two_item()
        time.sleep(2)

        elems = self._controller.check_cart_items()
        self.assertTrue(elems[0].text, self._controller.FIRST_PRODUCT.lower())
        self.assertTrue(elems[1].text, self._controller.SECOND_PRODUCT.lower())