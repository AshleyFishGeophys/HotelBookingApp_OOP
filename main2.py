from functions import *

hotel_ID = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_ID)

if hotel.available():
    print("Hotel is available.")
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        pass_given = input("Please enter CC password: ")
        if credit_card.authenticate(given_password=pass_given):
            print("CC validated successfully.")
            hotel.book()
            name = input("Enter your name: ")
            confirmation = ReservationConfirmation(customer_name=name, hotel_object=hotel)
            print(confirmation.generate())
            spa = input("So you want to book a spa package? ")
            if spa == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
        else:
            print("CC authentication failed.")
    else:
        print("There was a problem with your payment.")
else:
    print("Hotel is not available.")
