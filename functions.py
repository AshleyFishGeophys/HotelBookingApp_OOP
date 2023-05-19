import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
# Load cards as dictionary to treat each row as its own data associated with the cardholder name.
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationConfirmation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


# Class inheritance
# Parent = SecureCreditCard, child = CreditCard
# Checks card info using CC num and password
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


if __name__ == "__main__":
    print(df)
    hotel_ID = input("Enter the id of the hotel: ")
    hotel = Hotel(hotel_ID)

    if hotel.available():
        credit_card = SecureCreditCard(number="1234567890123456")
        if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
            pass_given = input("Please enter CC password: ")
            if credit_card.authenticate(given_password=pass_given):
                print("CC validated successfully.")
                hotel.book()
                name = input("Enter your name: ")
                confirmation = ReservationConfirmation(customer_name=name, hotel_object=hotel)
                print(confirmation.generate())
            else:
                print("CC authentication failed.")
        else:
            print("There was a problem with your payment.")
    else:
        print("Hotel is not available.")
