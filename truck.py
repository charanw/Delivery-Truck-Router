import datetime


class Truck:

    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.avg_speed = 18.0
        self.current_location = ""
        self.distance_traveled = 0.0
        self.cargo = []
        self.departure_time = datetime.datetime
        self.return_time = datetime.datetime

    def __str__(self):
        return self.truck_id
