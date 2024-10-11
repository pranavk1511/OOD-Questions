# Design a parking lot manager 

# Steps for OOD for parking lot 
# 1. Identify the classes
# 2. Identify Relationships 
# 3. Define Operations

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate, size):
        self.license_plate = license_plate
        self.size = size

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "CAR")

class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "TRUCK")

class Bike(Vehicle):
    def __init__(self,license_plate):
        super().__init__(license_plate, "BIKE")

class ParkingSpot:

    def __init__(self,spot,size):
        self.spot = spot
        self.size = size
        self.vehicle = None

    def can_fit(self,vehicle):
        if self.vehicle is not None:
            return False  
        if self.size == "Small" and isinstance(vehicle, Bike):
            return True
        elif self.size == "Medium" and isinstance(vehicle, (Car, Bike)):
            return True
        elif self.size == "Large" and isinstance(vehicle, (Truck, Car, Bike)):
            return True
        return False

    def park(self, vehicle):
        if self.can_fit(vehicle):
            self.vehicle = vehicle
            return True
        return False

    def remove(self):
        self.vehicle = None

class ParkingLevel:
    def __init__(self, level_id, num_spots):
        self.level_id = level_id
        self.spots = [ParkingSpot(i, "Large" if i < num_spots//3 else "Medium" if i < (2*num_spots)//3 else "Small") for i in range(num_spots)]
        
    def find_available_spot(self, vehicle):
        for spot in self.spots:
            if spot.can_fit(vehicle):
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_available_spot(vehicle)
        if spot is not None:
            spot.park(vehicle)
            return True
        return False

    def remove_vehicle(self, license_plate):
        for spot in self.spots:
            if spot.vehicle and spot.vehicle.license_plate == license_plate:
                spot.remove()
                return True
        return False

class ParkingLot:
    def __init__(self, levels):
        self.levels = levels

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                print(f"Vehicle {vehicle.license_plate} parked.")
                return True
        print(f"No available spot for vehicle {vehicle.license_plate}.")
        return False

    def remove_vehicle(self, license_plate):
        for level in self.levels:
            if level.remove_vehicle(license_plate):
                print(f"Vehicle {license_plate} removed.")
                return True
        print(f"Vehicle {license_plate} not found.")
        return False

# Example usage
if __name__ == "__main__":
    level1 = ParkingLevel(1, 10)
    level2 = ParkingLevel(2, 10)
    
    parking_lot = ParkingLot([level1, level2])
    
    car1 = Car("ABC123")
    car2 = Car("XYZ789")
    bike = Bike("MOTO567")
    
    parking_lot.park_vehicle(car1)  # Should park successfully
    parking_lot.park_vehicle(car2)  # Should park successfully
    parking_lot.park_vehicle(bike)  # Should park successfully
    
    parking_lot.remove_vehicle("XYZ789")  # Removes car with license "XYZ789"
    
# Key Points:
# Class Hierarchy: The Vehicle class is the base class, with Car, Motorcycle, and Truck extending it. Each parking spot checks the size compatibility of the vehicle before parking.
# Parking Levels: The parking lot is divided into multiple levels, each with multiple parking spots of different sizes.
# Spot Assignment: The ParkingSpot class ensures that vehicles are parked only in suitable spots.
# OOP Principles: Inheritance (e.g., Car inheriting from Vehicle), encapsulation (vehicle and spot properties), and abstraction (abstract class Vehicle) are used effectively.


    

