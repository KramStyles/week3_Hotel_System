from .room import Room
from .model import Model


class Booking(Model):
    _id = None
    room_id = None
    name = None
    paid = None

    @classmethod
    def create(cls, record):
        # Requirements:
        #   - The record argument will always be a dictionary representing a database record
        #   - Assign values from the record dictionary to the corresponding model attributes

        instance = cls()

        # Add your implementation here ...
        pass
    
    def room(self, db):
        # Requirements:
        #   - Select rooms from the database that has the room id set on this model as self.room_id
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Room model instance by calling the model's create method with the first record in the query results

        # Remove the pass statement below and add your implementation there ...
        pass
