import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    #  Class variable can be shared across all instances
    #  i.e. watermark is the company selling hotel reservations
    watermark = "The Real Estate Company"

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

    # Class method not associated with instance
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # Magic method
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
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
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}"""
        return content

    # Property method
    # Interacts with instance
    @property
    def the_customer_name(self):
        # Remove blanks and make f and l name capitalized
        name = self.customer_name.strip().title()
        return name

    # static method.
    # Like a function. Has no reference to class or class methods
    # Use when you want to do a utility less associated with class
    # Convert Euros to USD
    @staticmethod
    def convert(amount):
        return amount * 1.2


if __name__ == "__main__":
    hotel1 = Hotel(hotel_id="188")
    hotel2 = Hotel(hotel_id="134")
    hotel3 = Hotel(hotel_id="134")

    # Magic method.
    # hotel1 == hotel2 equivalent to Hotel.__eq__(hotel1, hotel2)
    print(hotel1 == hotel2)
    print(Hotel.__eq__(hotel1, hotel2))
    print(Hotel.__eq__(hotel2, hotel3))
