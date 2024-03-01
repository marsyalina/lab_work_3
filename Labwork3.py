'''
    Program purpose: To ask user to input data on Breekie Hotel Reservation System
    Programmer: NOOR MARSYALINA
    Date: 1 March 2024
'''

import datetime

Single = 100.00
Double = 150.00
Suite = 250.00
Breakfast= 20
Wifi = 10
Parking = 15

print("WELCOME TO BREEKIE HOTEL RESERVATION SYSTEM:")
print("Available Room Types:")
print("1. Single Room - RM 100 per night")
print("2. Double Room - RM 150 per night")
print("3. Suite Room - RM 250 per night")

room_type = input("Enter your choice (1 or 2 or 3): ")
number_room = int(input("Enter the number of rooms: "))
check_in_date = input("Enter your check-in date (YYYY-MM-DD): ")
check_out_date = input("Enter your check-out date (YYYY-MM-DD): ")

check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d")
check_out_date = datetime.datetime.strptime(check_out_date, "%Y-%m-%d")
num_of_nights = (check_out_date - check_in_date).days

if room_type == '1':
        total = Single * number_room * num_of_nights
elif room_type == '2':
        total = Double * number_room * num_of_nights
elif room_type == '3':
        total = Suite * number_room * num_of_nights
else:
    print("Invalid Option")
    exit()

print("Your total is: RM", total)
print("----------------------------------------------------------------------------------------")
print("HERE ARE SOME ADDITIONAL SERVICES FROM OUR HOTEL:")
print("1. Breakfast - RM 20 per person")
person = int(input("Enter the number of person: "))
print("2. Wifi - RM 10 per day")
print("3. Parking - RM 15 per day")

like = input("Would you like to add any additional service? (yes or no): ")

if like.lower() == 'yes':
    additional_service = input("Enter your choice (1 or 2 or 3): ")

    if additional_service == '1':
        total_service = Breakfast * person
    elif additional_service == '2':
        total_service= Wifi * num_of_nights
    elif additional_service == '3':
        total_service = Parking * num_of_nights

    else:
        print("Invalid Option")
        exit()

    print("Your total is: RM", total_service)
    print("----------------------------------------------------------------------------------------")
    print("THANK YOU FOR YOUR RESERVATION")
    print("HERE YOUR RESERVATION DETAIL:")
    print("Room Type: ", room_type)
    print("Number of Rooms: ", number_room)
    print("Check-In:",check_in_date)
    print("Check-Out:", check_out_date)

    print("Additional Service")
    print("Your total for additional service: RM", total_service)
    print("Reservation confirmed.Thank you for choosing our hotel. Enjoy your stay")


