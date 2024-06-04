# This class creates the truck object
class Trucks:
    def __init__(self, speed, miles, current_location, depart_time, packages):
        self.speed = speed
        self.miles = miles
        self.current_location = current_location
        self.time = depart_time
        self.depart_time = depart_time
        self.packages = packages

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (
            self.speed,
            self.miles,
            self.current_location,
            self.time,
            self.depart_time,
            self.packages,
        )
