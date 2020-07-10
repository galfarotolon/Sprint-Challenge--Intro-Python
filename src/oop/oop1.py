# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    #base class
    pass

class FlightVehicle(Vehicle):
    #inherits from vehicle
    pass

class Starship(FlightVehicle):
    #parent is flightvehicle, base is vehicle
    pass

class GroundVehicle(Vehicle):
    # inherit from vehicle
    pass

class Car(GroundVehicle):
    # parent is groundvehicle, goes up to vehicle as base
    pass

class Motorcycle(GroundVehicle):
    # parent is groundvehicle, goes up to vehicle as base
    pass

class Airplane(FlightVehicle):
    # parent is flightvehicle, goes up to vehicle as base
    pass