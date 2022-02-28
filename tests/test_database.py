import unittest
from __mocks__ import *

class TestHotel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = hotel_mock_data

    def test_hotel(self):
        print(self.data)