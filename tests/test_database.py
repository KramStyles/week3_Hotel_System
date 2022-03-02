import unittest

from database.table import Table
from .__mocks__ import *


class TestHotel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hotel = Table('name')
        cls.hotel.data[0] = hotel_mock_data


    def test_validate(self):
        self.assertEqual(self.hotel.validate(), f"You need to fill in the correct parameters {self.hotel.fields}")
        self.assertEqual(self.hotel.validate(names="Dennis hotels"),
                         f"The keys don't match. Check your input ({self.hotel.fields})")

        self.assertTrue(self.hotel.validate(name='Benis Hotel'))

    def test_insert(self):
        self.assertEqual(self.hotel.insert(), f"You need to fill in the correct parameters {self.hotel.fields}")
        self.assertEqual(self.hotel.insert(names="Dennis hotels"),
                         f"The keys don't match. Check your input ({self.hotel.fields})")
        self.assertEqual(self.hotel.insert(name="Dennis hotels"), {'name': 'Dennis hotels', '_id': 1})

    def test_select(self):
        self.hotel.insert(name="Decagon Hotels")
        self.assertEqual(self.hotel.select(_id=1), [{'name': 'Dennis hotels', '_id': 1}])
        self.assertEqual(self.hotel.select(name="Decagon Hotels"), [{'name': 'Decagon Hotels', '_id': 2}])
        self.assertEqual(self.hotel.select(_id=11), [])


class TestRoom(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rooms = Table('hotel_id', 'price', 'capacity')
        cls.rooms.data[0] = room_mock_data

    def test_validate(self):
        self.assertEqual(self.rooms.validate(), f"You need to fill in the correct parameters {self.rooms.fields}")
        self.assertEqual(self.rooms.validate(names="Dennis hotels"),
                         f"The keys don't match. Check your input ({self.rooms.fields})")

        self.assertEqual(self.rooms.validate(price=2), 'ok')

    def test_insert(self):
        self.assertEqual(self.rooms.insert(), f"You need to fill in the correct parameters {self.rooms.fields}")
        self.assertEqual(self.rooms.insert(names="Dennis hotels"),
                         f"The keys don't match. Check your input ({self.rooms.fields})")
        self.assertEqual(self.rooms.insert(hotel_id=3, price=1000, capacity=1), {'_id': 1, 'capacity': 1, 'hotel_id': 3, 'price': 1000})

    def test_select(self):
        self.assertEqual(self.rooms.select(_id=1), [{'_id': 1, 'capacity': 1, 'hotel_id': 3, 'price': 1000}])
        self.assertEqual(self.rooms.select(name="Decagon Hotels"), "The keys don't match. Check your input (('hotel_id', 'price', 'capacity'))")
        self.assertEqual(self.rooms.select(_id=11), [])


class TestBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rooms = Table('hotel_id', 'price', 'capacity')
        cls.rooms.data[0] = room_mock_data

    def test_validate(self):
        self.assertEqual(self.rooms.validate(), f"You need to fill in the correct parameters {self.rooms.fields}")
        self.assertEqual(self.rooms.validate(names="Dennis hotels"),
                         f"The keys don't match. Check your input ({self.rooms.fields})")

        self.assertEqual(self.rooms.validate(price=2), 'ok')

    def test_insert(self):
        self.assertEqual(self.rooms.insert(), f"You need to fill in the correct parameters {self.rooms.fields}")
        self.assertEqual(self.rooms.insert(names="Dennis hotels"),
                         f"The keys don't match. Check your input ({self.rooms.fields})")
        self.assertEqual(self.rooms.insert(hotel_id=3, price=1000, capacity=1),
                         {'_id': 1, 'capacity': 1, 'hotel_id': 3, 'price': 1000})

    def test_select(self):
        self.assertEqual(self.rooms.select(_id=1), [{'_id': 1, 'capacity': 1, 'hotel_id': 3, 'price': 1000}])
        self.assertEqual(self.rooms.select(name="Decagon Hotels"),
                         "The keys don't match. Check your input (('hotel_id', 'price', 'capacity'))")
        self.assertEqual(self.rooms.select(_id=11), [])


if __name__ == '__main__':
    unittest.main()

