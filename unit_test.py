import unittest
from go_to_url import *

class Test_reached_payment(unittest.TestCase):

    def setUp(self) :
        print('test suite start')


    def test_url_isPayment(self):
        expected = "https://www.agoda.com/book/payment/"
        self.assertTrue(expected in url)

    def tearDown(self):
        print("test suite ended")

if __name__ == '__main__':
    unittest.main()