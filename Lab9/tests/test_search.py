from pages.search_page import SearchPage
import unittest
from parameterized import parameterized
from config.config import TestData

class FindTest(unittest.TestCase):
    def setUp(self):        
        self._controller = SearchPage()
        self._controller.open_page(TestData.BASE_URL)

    def tearDown(self):
        self._controller.close()


    def test_search_by_category(self):
        self._controller.click_on_category()

        self.assertTrue(self._controller.check_availaility('product-main'), msg=f'error with categor')
        elem = self._controller.get_category_correctly()
        self.assertEqual(elem.text, self._controller.SEARCH_CATEGORY, msg=f'error with name category')

    def test_find_by_input_with_valid_value(self):
        self._controller.search_valid()
        self.assertTrue(self._controller.check_availaility('product-main'), msg=f'error with find by input with non empty value')

    def test_find_by_input_with_invalid_value(self):
        self._controller.search_invalid()
        self.assertFalse(self._controller.check_availaility('product-main'), msg=f'error with find by input with empty value')
        