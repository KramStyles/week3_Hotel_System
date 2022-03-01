from model import Model
from hotel import Hotel
from database import Database


class Room(Model):
    _id = None
    hotel_id = None
    price = None
    capacity = None

    @classmethod
    def create(cls, record):
        # Requirements:
        #   - The record argument will always be a dictionary representing a database record
        #   - Assign values from the record dictionary to the corresponding model attributes

        instance = cls

        # Add your implementation here ...
        instance._id = record['_id']
        instance.hotel_id = record['hotel_id']
        instance.price = record['price']
        instance.capacity = record['capacity']
        print(instance._id, instance.hotel_id, instance.price, instance.capacity)

    def hotel(self, db):
        # Requirements:
        #   - Select hotels from the database that has the hotel_id set on this model as self.hotel_id
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Hotel model instance by calling the model's create method with the first record in the query results

        # Remove the pass statement below and add your implementation there ...
        hotels = db.hotels
        print('Id is:', self._id)
        room_data = db.hotels.select(_id=self._id)
        if not room_data:
            return None
        else:
            return Hotel.create(room_data[0])


db = Database

rooms = db.rooms
rooms.insert(hotel_id=1, price=1500, capacity=1)
rooms.insert(hotel_id=2, price=2500, capacity=1)
rooms.insert(hotel_id=1, price=3000, capacity=2)
rooms.insert(hotel_id=2, price=4000, capacity=2)

Room.create(rooms.select(hotel_id=2)[0])
create = Room()
create.hotel(db)

hotels = db.hotels
hotels.insert(name='Chocolate Hotels')
hotels.insert(name='Strawberry Hotels')
hotels.insert(name='Hotel De La Paiz')

print(hotels.data)