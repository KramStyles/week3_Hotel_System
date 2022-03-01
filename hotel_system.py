from models import Room, Hotel, Booking
from database import Database

DB = Database()


class HotelSystem:
    def __init__(self, db):
        self.db = db

    def register_hotel(self, name):
        # Requirements:
        #   - Insert new hotel record into the database
        #   - Return a Hotel model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        hotel = self.db.hotels.insert(name=name)
        return Hotel.create(hotel)



    def add_room(self, hotel_id, **params):
        # Requirements:
        #   - Insert new room record into the database
        #   - Return a Room model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        params['hotel_id'] = hotel_id
        new_room = self.db.rooms.insert(**params)
        return Room.create(new_room)

    def get_room(self, room_id):
        # Requirements:
        #   - Select a room with the room_id argument from the database
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Room model instance by calling the model's create method with the first record in the query results

        # Remove the pass statement below and add your implementation there ...
        room = self.db.rooms.select(_id=room_id)
        if not room:
            return None
        else:
            return Room.create(room[0])

    def book_room(self, room_id, **params):
        # Requirements:
        #   - Insert new booking record into the database
        #   - Return a Booking model by calling the model's create method instance with the query result

        # Remove the pass statement below and add your implementation there ...

        params['room_id'] = room_id
        new_book = self.db.bookings.insert(**params)
        return print(Booking.create(new_book))


hs = HotelSystem(DB)
# hs.register_hotel('Boriton')
hs.add_room(hotel_id=1, price=10000, capacity=4)
hs.get_room(room_id=1)
hs.book_room(room_id=1, name='Michael', paid=True)