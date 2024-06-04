import datetime


# Creation of package class that stores the criteria of the packages
class Packages:
    # Initializing all the package attributes
    def __init__(
        self,
        ID,
        street,
        city,
        state,
        zip,
        deadline,
        weight,
        notes,
        status,
        departure_time,
        delivery_time,
    ):
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return (
            "ID: %s, %-20s, %s, %s,%s, Deadline: %s,%s,%s,Departure Time: %s,Delivery Time: %s"
            % (
                self.ID,
                self.street,
                self.city,
                self.state,
                self.zip,
                self.deadline,
                self.weight,
                self.status,
                self.departure_time,
                self.delivery_time,
            )
        )

    # This method updates the package status depending on the entered time
    def status_update(self, timeChange):
        if self.delivery_time == None:
            self.status = "Processing at the HUB"
        elif timeChange < self.departure_time:
            self.status = "Processing at the HUB"
        elif timeChange < self.delivery_time:
            self.status = "Out for Delivery"
        else:
            self.status = "Delivered"
        # Changes package 9 to the correct address
        if self.ID == 9:
            if timeChange > datetime.timedelta(hours=10, minutes=20):
                self.street = "410 S State St"
                self.zip = "84111"
            else:
                self.street = "300 State St"
                self.zip = "84103"
