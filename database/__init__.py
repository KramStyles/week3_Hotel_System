from table import Table


class Database:
    hotels = Table('name')
    rooms = Table('hotel_id', 'price', 'capacity')
    bookings = Table('room_id', 'name', 'paid')


#
# jon = Table('name', 'surname', 'middlename')
# jon.insert2(name="Jonathan", surname = "Kolawale")
# jon.insert2(name="John", surname = "Ola")
# # jon.insert2()
# print(jon.data2)

hotels = Table('name')
hotels.insert(name='Chocolate Hotels')
hotels.insert(name='Strawberry Hotels')

rooms = Table('hotel_id', 'price', 'capacity')
rooms.insert(hotel_id=2, price=4000, capacity=3)
rooms.insert(hotel_id=1, price=3000, capacity=2)
rooms.insert(hotel_id=2, price=3000, capacity=1)
print(rooms.data)

print(rooms.select(hotel_id = 2, price=4000))
