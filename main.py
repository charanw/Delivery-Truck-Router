# Created by Charan Williams

import datetime
import package
import packageHashMap
import getDistance
import truck
import time
import csv

packageMap = packageHashMap.PackageHashMap(40)
distanceList = []

with open('Package File.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[5] == 'EOD':
            row[5] = time.strftime("%I:%M %p", time.strptime('17:00', "%H:%M"))
        else:
            row[5] = time.strftime("%I:%M %p", time.strptime(row[5], "%I:%M %p"))

        packageMap.add_package(
            package.Package(int(row[0]), row[1], row[2], row[3], int(row[4]), row[5], float(row[6]), row[7]))
file.close()

with open('Distance Table.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        distanceList.append(row)
file.close()


def update_delivery_status(specified_time):
    all_packages = packageMap.get_all_packages()
    for package in all_packages:

        departureTime = package.truck.departure_time

        if departureTime < specified_time < package.deliveryTime:
            package.deliveryStatus = "En Route"
        elif specified_time < package.deliveryTime:
            package.deliveryStatus = "At the hub"
        elif specified_time >= package.deliveryTime:
            package.deliveryStatus = "Delivered"


print("Welcome to the package delivery system. Please see the calculated routes below:\n")


def deliver_packages(truck):
    hub = distanceList[1][0]
    truck.current_location = hub
    current_time = truck.departure_time
    cargo = truck.cargo
    print("The delivery route for " + str(truck) + ":\n")
    while len(cargo) > 0:
        closest_package = cargo[0]
        distance_to_closest_package = getDistance.get_distance(truck.current_location, closest_package.address,
                                                               distanceList)
        for package in cargo:
            package.truck = truck
            distance1 = getDistance.get_distance(truck.current_location, package.address, distanceList)
            distance2 = getDistance.get_distance(truck.current_location, closest_package.address, distanceList)
            if distance1 < distance2:
                closest_package = package
                distance_to_closest_package = distance1

        truck.current_location = closest_package.address
        print("Package ID:" + str(closest_package.id) + " Package Address: " + str(closest_package.address) + ", " + str(closest_package.city) + ", " + str(closest_package.state) + ", " + str(closest_package.zip))
        truck.distance_traveled += distance_to_closest_package

        time_to_deliver = datetime.timedelta(hours=(distance_to_closest_package / truck.avg_speed))
        current_time += time_to_deliver
        closest_package.deliveryStatus = "Delivered"
        closest_package.deliveryTime = current_time
        truck.cargo.remove(closest_package)

    distance_to_return_to_hub = getDistance.get_distance(truck.current_location, hub, distanceList)
    truck.distance_traveled += distance_to_return_to_hub
    truck.return_time = current_time + datetime.timedelta(hours=(distance_to_return_to_hub / truck.avg_speed))
    truck.current_location = hub
    print("\nDeparts At: " + str(truck.departure_time) + " Returns to Hub At: " + str(truck.return_time) + "\n" + "\n**********\n")


truck1 = truck.Truck("Truck 1")
truck1.cargo.extend(
    [packageMap.get_package(15), packageMap.get_package(29), packageMap.get_package(1), packageMap.get_package(13),
     packageMap.get_package(30), packageMap.get_package(31), packageMap.get_package(20),
     packageMap.get_package(40), packageMap.get_package(14), packageMap.get_package(16),
     packageMap.get_package(34), packageMap.get_package(27), packageMap.get_package(35), packageMap.get_package(7),
     packageMap.get_package(39), packageMap.get_package(19)])

truck2 = truck.Truck("Truck 2")
truck2.cargo.extend(
    [packageMap.get_package(18), packageMap.get_package(36), packageMap.get_package(3),
     packageMap.get_package(11), packageMap.get_package(8), packageMap.get_package(6),
     packageMap.get_package(17), packageMap.get_package(32), packageMap.get_package(12), packageMap.get_package(38),
     packageMap.get_package(5), packageMap.get_package(25), packageMap.get_package(26),
     packageMap.get_package(23), packageMap.get_package(37)])

truck3 = truck.Truck("Truck 3")
truck3.cargo.extend(
    [packageMap.get_package(9), packageMap.get_package(2), packageMap.get_package(33), packageMap.get_package(24),
     packageMap.get_package(10), packageMap.get_package(22), packageMap.get_package(21), packageMap.get_package(28),
     packageMap.get_package(4)])

current_datetime = datetime.datetime.now()
truck1.departure_time = datetime.datetime(current_datetime.year, current_datetime.month, current_datetime.day, hour=8,
                                          minute=0)
truck2.departure_time = datetime.datetime(current_datetime.year, current_datetime.month, current_datetime.day, hour=9,
                                          minute=5)
truck3.departure_time = datetime.datetime(current_datetime.year, current_datetime.month, current_datetime.day, hour=10,
                                          minute=20)

deliver_packages(truck1)
deliver_packages(truck2)

packageMap.get_package(9).address = "410 S State St"
packageMap.get_package(9).city = "Salt Lake City"
packageMap.get_package(9).zip = "84111"

deliver_packages(truck3)

terminate = 0

print("Total miles traveled by all trucks: " + str(
    truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled) + "\n" + "\n**********\n")

while terminate == 0:
    print("For more details, please type a menu option, then press 'Enter' to proceed: ")
    print("1. See final package statuses")
    print("2. See all package statuses at a specific time")
    print("3. Quit the program")
    user_input = input()
    if user_input == "1":
        end_of_day = datetime.datetime(current_datetime.year, current_datetime.month, current_datetime.day, hour=17,
                                       minute=0)
        update_delivery_status(end_of_day)
        print(packageMap)
    elif user_input == "2":
        print("Please enter a 24 hour time in the format 'hh:mm' (military time):")
        input_time = time.strptime(input(), "%H:%M")
        input_dateTime = datetime.datetime(current_datetime.year, current_datetime.month, current_datetime.day,
                                           input_time.tm_hour, input_time.tm_min)
        update_delivery_status(input_dateTime)
        print(packageMap)

    elif user_input == "3":
        terminate = 1
    else:
        print("Invalid input. Please enter a number between 1 and 3.")
