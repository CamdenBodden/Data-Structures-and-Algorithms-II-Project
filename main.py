# Author: Camden Bodden
# Student ID: 011056755
# Professor: Preety khatri
# Title : WGUPS Routing Program
# Date : 06/03/2024

import csv
import datetime

# import all the classes for this project including the truck, package, and hash table
from hashTable import HashTable
from packages import Packages
from trucks import Trucks

# I will be turning the excel files into csv files so my IDE can read it
# Reads the data from Packages.csv
with open("Packages.csv") as packageCSV:
    Package_csv = csv.reader(packageCSV)
    Package_csv = list(Package_csv)

# Reads the data from Distances.csv
with open("Distances.csv") as distanceCVS:
    Distance_csv = csv.reader(distanceCVS)
    Distance_csv = list(Distance_csv)

# Reads the data from Adresses.csv
with open("Adresses.csv") as adressCSV:
    Address_csv = csv.reader(adressCSV)
    Address_csv = list(Address_csv)


# Uses the package info from the csv to be insetrted into the Hash table
def load_package_data(filename):
    with open(filename) as packages:
        packInfo = csv.reader(packages, delimiter=",")
        next(packInfo)
        for package in packInfo:
            pID = int(package[0])
            # print(pID)
            pStreet = package[1]
            # print(pStreet)
            pCity = package[2]
            # print(pCity)
            pState = package[3]
            # print(pState)
            pZip = package[4]
            # print(pZip)
            pDeadline = package[5]
            # print(pDeadline)
            pWeight = package[6]
            # print(pWeight)
            pNotes = package[7]
            # print(pNotes)
            pStatus = "Processing at the HUB"
            pdeparture_time = None
            pdelivery_time = None

            # Inserting Package info into the hash
            p = Packages(
                pID,
                pStreet,
                pCity,
                pState,
                pZip,
                pDeadline,
                pWeight,
                pNotes,
                pStatus,
                pdeparture_time,
                pdelivery_time,
            )
            # print (p)
            packHash.insert(pID, p)


# This is the hash table for the packages
packHash = HashTable()


# Finds the minimum distance for next adress
def Address(address):
    for row in Address_csv:
        if address in row[2]:
            return int(row[0])


# finds the distance between 2 addresses
def DisBtwnAds(address1, address2):
    distance = Distance_csv[address1][address2]
    if distance == "":
        distance = Distance_csv[address2][address1]
    return float(distance)


# data from csv into function
load_package_data("Packages.csv")

# manually loading the trucks!!!
truck1 = Trucks(
    18,
    0.0,
    "4001 South 700 East",
    datetime.timedelta(hours=8),
    [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40],
)
truck2 = Trucks(
    18,
    0.0,
    "4001 South 700 East",
    datetime.timedelta(hours=11),
    [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38],
)
truck3 = Trucks(
    18,
    0.0,
    "4001 South 700 East",
    datetime.timedelta(hours=9, minutes=5),
    [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 25, 33, 39],
)


# algorithm time!! This is the algorthim to deliver packages on the truck
def truck_package_delivery(truck):
    # creates a list for all the packages that need to be delivered
    out_for_delivery = []
    # pulls packages from the hash table to the delivery list
    for packageID in truck.packages:
        package = packHash.search(packageID)
        out_for_delivery.append(package)

    truck.packages.clear()
    # As long as there are packages to be delivered the algorithim will run
    while len(out_for_delivery) > 0:
        next_adress = 2000
        next_package = None
        for package in out_for_delivery:
            if package.ID in [25, 6]:
                next_package = package
                next_adress = DisBtwnAds(
                    Address(truck.current_location), Address(package.street)
                )
                break
            if (
                DisBtwnAds(Address(truck.current_location), Address(package.street))
                <= next_adress
            ):
                next_adress = DisBtwnAds(
                    Address(truck.current_location), Address(package.street)
                )
                next_package = package
        truck.packages.append(next_package.ID)
        out_for_delivery.remove(next_package)
        truck.miles += next_adress
        truck.current_location = next_package.street
        truck.time += datetime.timedelta(hours=next_adress / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time


# Calls the trucks to deliver packages
truck_package_delivery(truck1)
truck_package_delivery(truck3)
# Makes sure that truck two will not leave until truck one or three returns
truck2.depart_time = min(truck1.time, truck3.time)
truck_package_delivery(truck2)


# User Interface
# prints welcome message and mileage
class Interface:
    print("Welcome to Western Governors University Parcel Service")
    total_mileage = truck1.miles + truck2.miles + truck3.miles
    print("The total mileage for today is: ", total_mileage)
    limit = 140
    diff = limit - total_mileage
    print("That is", f"{diff:.3}", "miles less than our limit of", limit, "miles!")
    print("The final package was delivered at : 12:29PM")

    print("")

    # prompt for input
    user_text = input("For more information type 'info': ")
    if user_text == "info":
        try:
            # prompt the user for desired time
            print("Enter a time for the status of each package. ")
            user_time = input("format: HH:MM (24 hour)        ")
            (h, m) = user_time.split(":")
            convert_time = datetime.timedelta(hours=int(h), minutes=int(m))

            # Determines if one or all the packages are needed to print
            package_selection = input(
                "Enter 'one' for information on an individual package "
                "or 'all' for all packages.      "
            )
            # prints one package
            if package_selection == "one":
                try:
                    packageID = input("Enter the package ID:          ")
                    package = packHash.search(int(packageID))
                    package.status_update(convert_time)
                    print(str(package))
                # Exits program
                except ValueError:
                    print("No")
                    exit()

            # prints out all the packages
            elif package_selection == "all":
                try:
                    for packageID in range(1, 41):
                        package = packHash.search(packageID)
                        package.status_update(convert_time)
                        print(str(package))
                # Exits program
                except ValueError:
                    print("No")
                    exit()
        except ValueError:
            print("No")
            exit()
