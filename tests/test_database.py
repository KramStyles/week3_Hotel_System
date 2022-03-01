import unittest
from __mocks__ import *
from database.table import Table


class TestHotel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = hotel_mock_data
        cls.hotel = Table('name')
        # cls.rooms = Table('hotel_id', 'price', 'capacity')
        # cls.bookings = Table('room_id', 'name', 'paid')

    def test_validate(self):
        self.assertEqual(self.hotel.validate(), f"You need to fill in the correct parameters {self.hotel.fields}")
        self.assertEqual(self.hotel.validate(names="Dennis hotels"), f"The keys don't match. Check your input ({self.hotel.fields})")

        self.assertTrue(self.hotel.validate(name='Benis Hotel'))

    def test_insert(self):
        self.assertTrue()



if __name__ == '__main__':
    unittest.main()

# Todo: How to fix __mock__ error
# Todo: Check connection of Modules to database