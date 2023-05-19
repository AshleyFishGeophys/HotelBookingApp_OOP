from functions import *

hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")
hotel3 = Hotel(hotel_id="134")

# Magic method.
# hotel1 == hotel2 equivalent to Hotel.__eq__(hotel1, hotel2)
print(hotel1 == hotel2)
print(Hotel.__eq__(hotel1, hotel2))
print(Hotel.__eq__(hotel2, hotel3))
