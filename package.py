import datetime
from truck import Truck


class Package:
    def __init__(self, id, address, city, state, zip, deliveryDeadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        self.notes = notes
        self.deliveryTime = datetime.datetime.now()
        self.deliveryStatus = "At the Hub"
        self.truck = Truck

    def __str__(self):
        return "Package ID: {self.id} \t Address: {self.address:40} \t City: {self.city:20} \t State: {self.state} \t Zip: {self.zip} \t Delivery Deadline: {self.deliveryDeadline} \t Weight: {self.weight} \t Notes: {self.notes:60} \t Delivery Status: {self.deliveryStatus:15} \t Delivery Time: {formatted_time}".format(self=self, formatted_time=self.deliveryTime.strftime('%I:%M %p'))