import unittest

from database import  Database
import models
from .__mocks__ import *


class TestHotel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hotel = models.Hotel
        cls.hotel.data = hotel_mock_data
        cls.hotel.data['_id'] = 1

    def test_create(self):
        try:
            self.assertIsInstance(self.hotel.create(self.hotel.data), models.Hotel)
            self.assertEqual(self.hotel.create(self.hotel.data).name, "Test Hotel")
        except TypeError as err:
            print("A dictionary is expected", err)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.hotel = None


class TestRoom(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.room = models.Room
        cls.room.data = room_mock_data
        cls.room.data['_id'] = 1
        cls.room.data['hotel_id'] = 3
        cls.DB = Database

    def test_create(self):
        try:
            self.assertIsInstance(self.room.create(self.room.data), models.Room)
            self.assertEqual(self.room.create(self.room.data).capacity, 5)
        except TypeError as err:
            print("A dictionary is expected", err)

    # def test_room(self):
    #     try:
    #         # {'paid': False, 'name': 'Jane Doe', '_id': 1}
    #         # self.assertIsInstance(self.booking.create(self.booking.data), models.Booking)
    #         # self.assertFalse(self.booking.create(self.booking.data).paid)
    #         self.assertEqual(self.booking.room(self, self.DB), '')
    #     except TypeError as err:
    #         print("A dictionary is expected", err)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.hotel = None


class TestBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.booking = models.Booking
        cls.booking.data = booking_mock_data
        cls.booking.data['_id'] = 1
        cls.booking.data['room_id'] = 3
        cls.DB = Database

    def test_create(self):
        try:
            self.assertIsInstance(self.booking.create(self.booking.data), models.Booking)
            self.assertFalse(self.booking.create(self.booking.data).paid)
        except TypeError as err:
            print("A dictionary is expected")

    # def test_room(self):
    #     try:
    #         # {'paid': False, 'name': 'Jane Doe', '_id': 1}
    #         # self.assertIsInstance(self.booking.create(self.booking.data), models.Booking)
    #         # self.assertFalse(self.booking.create(self.booking.data).paid)
    #         self.assertEqual(self.booking.room(self, self.DB), '')
    #     except TypeError as err:
    #         print("A dictionary is expected", err)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.booking = None

if __name__ == '__main__':
    unittest.main()
