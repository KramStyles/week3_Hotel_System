import unittest
import models

from database import Database
from hotel_system import HotelSystem



class TestHotelSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = Database
        cls.hs = HotelSystem(cls.db)

    def test_register_hotel(self):
        try:
            self.assertIsInstance(self.hs.register_hotel('Benigton'), models.Hotel)
            self.assertEqual(self.hs.register_hotel('Benigton').name, "Benigton")
        except TypeError as err:
            print("Check your input", err)


    def test_add_room(self):
        try:
            self.assertIsInstance(self.hs.add_room(hotel_id=1, price=10000, capacity=4), models.Room)
            self.assertEqual(self.hs.add_room(hotel_id=1, price=10000, capacity=4).price, 10000)
        except TypeError as err:
            print("A dictionary is expected", err)

    def test_get_room(self):
        try:
            self.assertIsInstance(self.hs.get_room(room_id=1), models.Room)
            self.assertEqual(self.hs.get_room(room_id=1).price, 10000)
        except TypeError as err:
            print("Check your input", err)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db = None
        cls.hs = None


if __name__ == '__main__':
    unittest.main()