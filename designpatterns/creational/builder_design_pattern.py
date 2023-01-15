"""
# Creational design patter https://youtu.be/MrrrtQT_8SE

Creational is used when we create a very 
  - complex design
  - configuration
Eg:
  - Building a complex object like House. It can have many configurations.
  - Building a device. Mobile/PC/Laptop. Constructor can be initiated with any number of things like it can have touch, 4 RAMS, No RAMS, etc, etc

Steps: There are 4 components - 
  1. Define class.EG: Desktop and its variables & parts
  2. Define DesktopBuilder so that concreate builders know that which all functions needs to be implemented
  3. Create some concreate builder. Eg: DellDesktopBuilder, HPDesktopBuilder, etc
  4. Director: It will take Specific builder (DellDesktopBuilder) and build desktop.

"""