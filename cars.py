# # Snake_case is the naming convention for variables in Python


# # Variables and Data Types

# brand = "Ford"  # String
# model_year = 2020  # Integer
# price = 50000.00  # Float
# is_new = True  # Boolean
# cars = ["Ford", "Toyota", "Chevrolet"]  # List
# car_information = {
#     "brand": "Ford",
#     "model_year": 2020,
#     "price": 50000.00,
#     "is_new": False
# }  # Dictionary

# # String concatenation
# car_year = "10"
# car_info = f"The car is {car_year} years old."
# print(car_info)

# # Math operations
# h = 1 + 1  # Addition
# y = 2 - 1  # Subtraction
# z = 2 * 2  # Multiplication
# a = 4 / 2  # Division
# d = 5 // 2  # Floor division
# b = 5 % 2  # Modulus
# c = 2 ** 3  # Exponent
# print(h, y, z, a, d, b, c)

# # Accessing elements in a list
# vehicle = ["car", "truck", "motorcycle"]
# # Adding to a list
# vehicle.append("bus")

# print(vehicle[1])  # truck
# print(vehicle)

# # Accessing elements in a dictionary
# car = {
#     "brand": "Ford",
#     "model_year": 2020,
#     "price": 50000.00,
#     "is_new": False
# }
# # Adding to a dictionary
# car["model_year"] = 2021
# print(car["model_year"])  # 2021


# # Constants
# # Writing constants in all caps is a convention in Python to indicate that the variable should not be changed
# TAX_RATE = 0.06

# # Functions

# # Function definition, takes in 2 paramaters


# def start_car(car_1, car_2):
#     print(f"Attempting to start {car_1} ...")
#     print(f"Attempting to start {car_2} ...")


# # Function call with the 2 arguments being passed in
# start_car("Ford", "Toyota")

# # If statements
# if brand == "Ford":
#     print("The brand is Ford")
# elif brand == "Toyota":
#     print("The brand is Toyota")
# else:
#     print("The brand is neither Ford nor Toyota")

# # Terenary
# status = "new" if is_new else "used"
# print(status)

# # For loops
# carros = ["Ford", "Toyota", "Chevrolet"]
# for cars in carros:
#     print("cars", car)

# # Range
# for i in range(6):
#     print(i)

# '''

# fuel = 5
# while fuel > 0:
#     print(f"Fuel level is {fuel}")
#     fuel -= 1

# while True:
#     command = input("Enter 'stop' to stop the car: ")
#     if command == "stop":
#         print("Car stopped.")
#         break
#     else:
#         print("Car is moving...")

# '''

# # Classes


# class Car:
#     def __init__(self, brand: str, year: int):
#         self.brand = brand
#         self.year = year

#     def start(self):
#         print(f"Your car is a {self.brand} mustang, {self.year}")


# new_car = Car("Ford", 2020)
# print(new_car.brand)
# print(new_car.year)
# new_car.start()


# try:
#     x = 5 / 0
#     print(x)
# except Exception as e:
#     print("Cannot divide by zero", e)

# grocery_list = ["apple", "banana", "orange", "grapes", "mango"]
# basket = ["apple", "banana"]

# grocery_list = [item for item in grocery_list if item not in basket]

# for item in basket:
#     if item in grocery_list:
#         grocery_list.remove(item)

# print(grocery_list)
