#Defining Variables for Indian Railway System



train_name = "Rajdhani Express"
train_number = 12301
ticket_price = 2450.50
is_ac_available = True 
seat_numbers = [1, 2, 3, 4, 5] 

# Showing the Details using print Function

# print("Train Name:",train_name) 
# print("Train Number:",train_number) 
# print("Ticket Price:",ticket_price)
# print("AC Availability:",is_ac_available)
# print("Seat Numbers:",seat_numbers) 

# # show the data types of the variables using Function
# print("The data type of train_name: ",type(train_name))
# print("The data type of train_number: ",type(train_number))
# print("The data type of ticket_price: ",type(ticket_price))
# print("The data type of is_ac_available: ",type(is_ac_available))
# print("The data type of seat_numbers: ",type(seat_numbers))

# # Getting passenger information
# print("=== Indian Railway Booking System ===")
# passenger_name = input("Enter passenger name: ")
# age = int(input("Enter age: "))
# destination = input("Enter destination: ")

# # Display booking confirmation 
# print("\n=== Booking Details ===")
# print(f"Passenger: {passenger_name}")
# print(f"Age: {age}")
# print(f"Destination: {destination}")
# print("Booking confirmed!")

# Arthimetic operators

# base_price = 1500
# service_charge = 100
# total_price = base_price + service_charge

# print(f"Base Price: ₹{base_price}")
# print(f"Service Charge: ₹{service_charge}")
# print(f"Total Price: ₹{total_price}")

# # Comparsion operators
# passenger_age = 25
# senior_citizen_age = 60
# is_senior = passenger_age >= senior_citizen_age

# print(f"\n Is passenger senior citizen? {is_senior}")

# Logical Operators

# has_ticket = True
# has_id_proof = True
# can_board = has_ticket and has_id_proof

# print(f"Can Board Train? {can_board}")

# Control Flow - If Statments

# Age based Pricings

# Age = int(input("Enter passenger age: "))

# if Age < 5:
#     price = 0
#     category = "Infant (Free)"
# elif Age < 12:
#     price = 750
#     category = "Child (50% Discount)"
# elif Age >= 60:
#     price = 1200
#     category = "Senior Citizen (20% Discount)"
# else:
#     price = 1500
#     category = "Adult"

# print (f"Category: {category}")
# print(f"Ticket Price: ₹{price}")

# For Loop - Display available trains

# trains = [{"name": "Rajdhani Express","number":12301 ,"destination":"New Delhi"},
#         {"name": "Shatabi Express","number":12001,"destination":"Chennai"},
#         {"name": "Duronto Express","number":12291,"destination":"Mumbai"}]

# print("Available Trains: ")
# for train in trains:
#     print(f"{train['number']} - {train['name']} to {train['destination']}")

# While Loop - Booking System Menu 

# print("\n=== Booking Menu ===")
# choice = 0

# while choice != 3:
#     print("1. Book Ticket")
#     print("2. Check Status")
#     print("3. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("Booking ticket .....")
#     elif choice == 2:
#         print("Checking Status")
#     elif choice == 3:
#         print("Thank you for using Indian Railways!")
#     else:
#         print("Invalid Choice!")


# Ticket Price Calculator

# def calculate_ticket_price(distance,class_type):
#     base_rate = 0.5

#     if class_type == "Sleeper":
#         multiplier = 1.0
#     elif class_type == "AC 3 Tier":
#         multiplier = 1.5
#     elif class_type == "AC 2 Tier":
#         multiplier = 2.0
#     elif class_type == "AC 1 Class":
#         multiplier = 3.0
#     else:
#         multiplier = 1.0

#     price = distance * base_rate * multiplier

#     return round(price,2)

# distance = 500
# class_type = "Sleeper"
# price = calculate_ticket_price(distance,class_type)

# print(f"Price for {distance}km in {class_type}:₹{price}")

# Ticket Booking 

# def book_ticket(passenger_name,age,destination,class_type = "Sleeper"):
#     ticket = {"Passenger_Name": passenger_name,"Age":age,"Destination":destination,"Booking ID":f"BK{hash(passenger_name)% 10000:04d}"}
#     return ticket

# def get_passenger_details(*args,**kwargs):
#     print("Positional arguments: ",args)
#     print("Keyword arguments: ",kwargs)

# ticket1 = book_ticket("Rahul Kumar",28,"Mumbai")
# ticket2 = book_ticket("Priya Singh",32,"Delhi","AC 3 Tier")

# print("\nTicket 1: ",ticket1)
# print("Ticket 2: ",ticket2)

# get_passenger_details("Rahul",28,"Mumbai",class_type = "Sleeper",meal_preference = "Veg")

#List

# states = ["Maharashtra", "Kerala", "Punjab","Tamil Nadu","Gujarat"]

# print("Original List:", states)

# # states.append("Karnataka")
# # states.insert(2, "Rajasthan")
# # print("After Append & Insert:", states)

# # Extend with another list
# states.extend(["Goa","Bihar"])
# print("After Extend:", states)

# # Remove elements
# states.remove("Punjab")
# popped = states.pop()
# print("Removed Element:", popped)
# print("After Remove & Pop:", states)

# Sorting & Reversing------------------------------------------------------------------------------

# states.sort()
# print("Sorted List:", states)
# states.reverse()
# print("Reversed List:", states)

# # Index & Count------------------------------------------------------------------------------
# print("Index of Kerala:", states.index("Kerala"))
# print("Index of Kerala:", states.count("Kerala"))

# # Copy & Clear------------------------------------------------------------------------------
# copy_status = states.copy()
# print("Copied List:", copy_status)
# states.clear()
# print("Cleared List:",states)

# Tulpe------------------------------------------------------------------------------
# cities = ("Mumbai","Delhi","Bengaluru","Chennai","Kolkata","Mumbai")

# print("Tulpe:", cities)

# # Count------------------------------------------------------------------------------
# print("Count of Mumbai:", cities.count("Mumbai"))

# #Index------------------------------------------------------------------------------
# print("Index of Chennai:", cities.index("Chennai"))

# # Length------------------------------------------------------------------------------
# print("Length:", len(cities))

# # Membership------------------------------------------------------------------------------
# print("Delhi in tulpe?", "Delhi" in cities)

# #Min & Max (alphabetical)
# print("Min:", min(cities))
# print("Max:", max(cities))

# Dictionary------------------------------------------------------------------------------
# capitals = {
#    "Maharashtra": "Mumbai",
#    "Kerala": "Thiruvananthapuram",
#    "Tamil Nadu": "Chennai",
#    "Gurjarat": "Gandhinagar"
# }

# print ("Dictionary:",capitals)

# # Get & Access
# print("Capital of Kerala:", capitals.get("Kerala"))

# # Keys, Values, Items
# print("States:", capitals.keys())
# print("Capitals:", capitals.values())
# print("Pairs:", capitals.items())

# Update & Add------------------------------------------------------------------------------
# capitals.update({"Karnataka": "Bengaluru"})
# capitals["Punjab"] = "Chandigarh"
# print("After Update:",capitals)

# # Remove------------------------------------------------------------------------------
# capitals.pop("Tamil Nadu")
# capitals.popitem()
# print("After Pop & Popitem:",capitals)

# # Copy & Clear------------------------------------------------------------------------------
# copy_caps = capitals.copy()
# capitals.clear()
# print("Copied:",copy_caps)
# print("Cleared:",capitals)

# Set 
# languages = {"Hindi","English","Marathi","Tamil","Telugu"}

# print("Original Set:", languages)

# # Add & Remove
# languages.add("Gurjarati")
# languages.discard("English")
# print("After Add & Discard:",languages)

# # Remove (error if not present)
# languages.remove("Hindi")

# # Set Operations
# south = {"Tamil","Telugu","Kannada"}
# print("Union:", languages.union(south))
# print("Intersection:",languages.intersection(south))
# print("Difference:",languages.difference(south))
# print("Symmertic Difference:", languages.symmetric_difference(south))

# # Copy & Clear
# copy_lang = languages.copy()
# languages.clear()
# print("Copied:", copy_lang)

# String
# movie = "Sholay is a Classic Bollywood Movie"

# print("Original:", movie)

# # Case
# # print(movie.upper())
# # print(movie.lower())
# # print(movie.title())
# # print(movie.capitalize())
# # print(movie.swapcase())

# # # Check
# # print(movie.startswith("Sholay"))
# # print(movie.endswith("Movie"))
# # print("Is Alpha?",movie.isalpha())
# # print("Is Digit?", movie.isdigit())

# # Find & Replace
# print("Find 'Classic':", movie.find("Classic"))
# print(movie.replace("Classic","Legendary"))

# # Split & Join
# words = movie.split()
# print("Split:", words)
# joined = "-".join(words)
# print("Joined:",joined)

# # Strip
# line = "    Jai Hind       "
# print("Stripped:", line.strip())
# print("Left Strip:", line.strip())
# print("Right Strip:", line.rstrip())

# # Count & Index
# print("Count of 'o':", movie.count("o"))
# print("Index of 'Bollywood':", movie.index("Bollywood"))

# # Length
# print("Length:", len(movie))

# Date & Time
# import datetime

# # Current date & time
# now = datetime.datetime.now()
# print("Now:",now)

# # Today
# today = datetime.date.today()

# # Specific date (Republic day)
# republic_day = datetime.date(1950,1,26)
# print("Republic Day:", republic_day.strftime("%d-%B-%Y"))

# # Time Difference
# diff = today - republic_day
# print("Days since Republic Day:",diff.days)

# # Current components
# print("Year:",now.year)
# print("Month:",now.month)
# print("Day:", now.day)
# print("Hour:", now.hour)
# print("Minute:",now.minute)
# print("Second:", now.second)

# # Create a time object
# t = datetime.time(10, 30, 15)
# print ("Custom Time:", t)

# # Combine date & Time
# dt = datetime.datetime.combine(today,t)

# # Formatting 
# print("Formatted:",now.strftime("%A, %d %B %Y, %I:%M %p"))

# Calculated Discounts

# calculate_discount = lambda price,discount_percentage :price * (1 - discount_percentage/100)

# original_price = 1500

# discounted_price = calculate_discount(original_price,20)

# print(f"Original: ₹{original_price},Discounted Price: ₹{discounted_price}")

# train = [
#     {"name":"Rajdhani","price":2500,"duration":16},
#     {"name":"Shatabdi","price":1800,"duration":8},
#     {"name":"Duronto","price":2000,"duration":12}
# ]

# # map

# train_names = list(map(lambda x: x['name'],train))
# print(f"\nTrain Names : {train_names}")

# # filter

# affordable_trains = list(filter(lambda x: x['price']< 2200,train))
# print("Affordable Trains: ",[t["name"] for t in affordable_trains])

# # sorted
# sorted_by_price = sorted(train,key=lambda x: x["price"])
# print("Sorted by Price: ",[t["name"] for t in sorted_by_price])

# OOP based Train System

# class Train:
#     def __init__(self,train_number,name,source,destination,total_seats):
#         self.train_number = train_number
#         self.name = name
#         self.source = source
#         self.destination = destination
#         self.total_seats = total_seats
#         self.available_seats = total_seats

#     def display_info(self):
#         print(f"{self.train_number} - {self.name}")
#         print(f"Route: {self.source} to {self.destination}")
#         print(f"Available Seats: {self.available_seats}/{self.total_seats}")

#     def book_seats(self):
#         if self.available_seats > 0:
#             self.available_seats -= 1
#             return True
#         return False

# train1 = Train(12301,"Rajdhani Express","Howrah","New Delhi",500)
# train2 = Train(12001,"Shatabdi Express","Chennai","Bangalore",400)

# print("==Train Information==")
# train1.display_info()
# print()
# train2.display_info()

# if train1.book_seats():
#     print("Seat Booked successfully in Rajdhai Express!")
#     train1.display_info()

# class Train:
#     def __init__(self,train_number,name,source,destination):
#         self.train_number = train_number
#         self.name = name
#         self.source = source
#         self.destination = destination

#     def get_info(self):
#         return f"{self.train_number} - {self.name}"

# class ExpressTrain(Train):
#      def __init__(self,train_number,name,source,destination,max_speed):
#         super().__init__(train_number,name,source,destination)
#         self.max_speed = max_speed

#      def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info} Max Speed: {self.max_speed} km/h"

# class PassengerTrain(Train):
#      def __init__(self, train_number, name, source, destination, stops):
#         super().__init__(train_number, name, source, destination)
#         self.stops = stops

#      def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info} (Stops: {len(self.stops)})"

# express = ExpressTrain(12301,"Rajdhani Express","Howrah","New Delhi",130)
# passenger = PassengerTrain(11001,"Intercity Express","Mumbai","Pune",["Lonavala","Khandala"])

# print("==Train Types==")
# print(f"Express Train:{express.get_info()}")
# print(f"Passenger Train: {passenger.get_info()}")