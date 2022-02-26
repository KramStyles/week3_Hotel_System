from models import Room, Hotel, Booking


class HotelSystem:
    def __init__(self, db):
        self.db = db

    def register_hotel(self, name):
        # Requirements:
        #   - Insert new hotel record into the database
        #   - Return a Hotel model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        pass

    def add_room(self, hotel_id, **params):
        # Requirements:
        #   - Insert new room record into the database
        #   - Return a Room model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        pass

    def get_room(self, room_id):
        # Requirements:
        #   - Select a room with the room_id argument from the database
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Room model instance by calling the model's create method with the first record in the query results

        # Remove the pass statement below and add your implementation there ...
        pass

    def book_room(self, room_id, **params):
        # Requirements:
        #   - Insert new booking record into the database
        #   - Return a Booking model by calling the model's create method instance with the query result

        # Remove the pass statement below and add your implementation there ...
        pass
