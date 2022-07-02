"""
This is a creational design pattern
The creational of class instance is handled by a separate class.
In this way, the other codebase/clients/users of those classes are not tightly coupled 
and dont have to deal with how to get an instance of class
"""

# -------------------------------- Without factory pattern --------------------------------------
# ourlibrary.py
class Vehicle:
  def about(self):
    raise NotImplementedError()

class Bike(Vehicle):
  def about(self):
    print("My name is bike!")

class Car(Vehicle):
  def about(self):
    print("My name is car!")

# other part of code that uses the above classes
vehicle_type = input("Enter a vehicle type:- ")
if(vehicle_type == "car"):
  vehicle = Car()
elif vehicle_type == "bike":
  vehicle = Bike()
# use the instance
vehicle.about()

"""
imagine we are using this vehicle classes in 10+ modules

1. With the above code, the disadvantage is - 
  a. We have to write the code for creating of clasess & ifelse in all 10 modules where we want to use the vehicles
2. suppose in future, we need to support 2 new vehicles:- bus & truck, then -
  a. we will create 2 new class Bus & Truck (this is fine)
  b. We also have to update other part part of code where we want to support the new vehicles. 
  (since we have used the class at 10+ modules in our code, then we have to update at all those modules & add ifelse there which will be a huge task)
  c. So, instead we can abstract out the class creation of vehicle in a new class factory and pass the config to that class to get an instance of classes.
""" 
# -------------------------------- With factory pattern of above code --------------------------------------

# ourlibrary.py 
class Vehicle:
  def about(self):
    raise NotImplementedError()

class Bike(Vehicle):
  def about(self):
    print("My name is bike!")

class Car(Vehicle):
  def about(self):
    print("My name is car!")

class VehicleFactory():
  @staticmethod
  def get_vehicle(vehicle_type):
    vehicle = None
    if(vehicle_type == "car"):
      vehicle = Car()
    elif vehicle_type == "bike":
      vehicle = Bike()
    else:
      print("INVALID VEHICLE")
    return vehicle
    
# other part of code that uses the above classes
vehicle_type = input("Enter a vehicle type:- ")
vehicle = VehicleFactory.get_vehicle(vehicle_type)
# use the instance
vehicle.about()

# -------------------------------- With factory pattern of above code with 2 new vehicle --------------------------------------

# ourlibrary.py 
class Vehicle:
  def about(self):
    raise NotImplementedError()

class Bike(Vehicle):
  def about(self):
    print("My name is bike!")

class Car(Vehicle):
  def about(self):
    print("My name is car!")

class Bus(Vehicle):
  def about(self):
    print("My name is bus!")

class Truck(Vehicle):
  def about(self):
    print("My name is truck!")


class VehicleFactory():
  @staticmethod
  def get_vehicle(vehicle_type):
    vehicle = None
    if(vehicle_type == "car"):
      vehicle = Car()
    elif vehicle_type == "bike":
      vehicle = Bike()
    elif vehicle_type == "bus":
      vehicle = Bus()
    elif vehicle_type == "truck":
      vehicle = Truck()
    else:
      print("INVALID VEHICLE")
    return vehicle
    
# other part of code that uses the above classes
vehicle_type = input("Enter a vehicle type:- ")
vehicle = VehicleFactory.get_vehicle(vehicle_type)
# use the instance
vehicle.about()

"""
As we can see, we just had to update our factory and all 10 module is unchanged;
"""