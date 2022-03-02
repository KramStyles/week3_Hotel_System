from .model import Model
# from database import Database

class Hotel(Model):
    _id = None
    name = None

    @classmethod
    def create(cls, record):
        # Requirements:
        #   - The record argument will always be a dictionary representing a database record
        #   - Assign values from the record dictionary to the corresponding model attributes
        instance = cls()

        # Add your implementation here ...
        instance._id = record['_id']
        instance.name = record['name']

        return instance




# db = Database
#
# hotels = db.hotels
# hotels.insert(name='Chocolate Hotels')
# hotels.insert(name='Strawberry Hotels')
# hotels.insert(name = 'Hotel De La Paiz')
#
# Hotel.create(hotels.select(name='Chocolate Hotels')[0])
