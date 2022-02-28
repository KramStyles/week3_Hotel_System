from table import Table


class Database:
    hotels = Table('name')
    rooms = Table('hotel_id', 'price', 'capacity')
    bookings = Table('room_id', 'name', 'paid')


hotels = Database.hotels
hotels.insert(name='Beniton Hotels')
hotels.insert(name='Paris Hotels')
print(hotels.data)
