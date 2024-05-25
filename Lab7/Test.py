import unittest
import requests

class MounteBankClass:
    def __init__(self):
        self._host = "http://localhost:4545"
        self._url = "/api/currency"
        
    def get_currency_rate(self):
        response = requests.get(self._host + self._url)
        response.raise_for_status()
        return (response.json())
            
class CurrencyConversionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._controller = MounteBankClass()    
        self._exchange_rate = self._controller.get_currency_rate()
        
        self._ERROR_CURRENCY_MSG = "Error"

        self._rates = {
            'RUB': '1.00',  
            'USD': '89.7',
            'CYN': '12.3'
        }

    def Convert(self, first, second, amount):
        if first not in self._rates or second not in self._rates:
            return self._ERROR_CURRENCY_MSG
        
        self._rate = float(self._rates[first]) / float(self._rates[second])

        converted_amount = amount * self._rate
        return converted_amount
   
    def test_from_RUB_to_USD(self):
        self._result = self.Convert("RUB", "USD", 350)
        
        self.assertEqual(4, round(self._result), msg="Error: from RUB to USD ")
    
    def test_from_RUB_to_CYN(self):
        self._result = self.Convert("RUB", "CYN", 5000)
        
        self.assertEqual(407, round(self._result), msg="Error: from rubles to euros ")


    def test_from_USD_to_RUB(self):
        self._result = self.Convert("USD", "RUB", 100)

        self.assertEqual(8970, round(self._result), msg="Error: from USD to RUB ")

    def test_from_USD_to_CYN(self):
        self._result = self.Convert("USD", "CYN", 1000)
        
        self.assertEqual(7293, round(self._result), msg="Error: from USD to CYN ")


    def test_from_CYN_to_RUB(self):
        self._result = self.Convert("CYN", "RUB", 100)

        self.assertEqual(1230, round(self._result), msg="Error: from CYN to RUB")

    def test_from_CYN_to_USD(self):
        self._result = self.Convert("CYN", "USD", 500)

        self.assertEqual(69, round(self._result), msg="Error: from CYN to USD")    