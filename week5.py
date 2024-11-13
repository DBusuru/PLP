# Assignment 1: Design Your Own Class

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def take_photo(self):
        print(f"Taking a photo with {self.model}...")

# Derived class
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a high-resolution photo with {self.camera_megapixels}MP camera on {self.model}.")

# Creating instances
basic_phone = Smartphone("GenericBrand", "BasicModel", "64GB")
advanced_phone = AdvancedSmartphone("SuperBrand", "AdvancedModel", "256GB", 108)

# Using methods
basic_phone.make_call("123-456-7890")
basic_phone.take_photo()
advanced_phone.make_call("987-654-3210")
advanced_phone.take_photo()


# Activity 2: Polymorphism Challenge

# Base class
class Vehicle:
    def move(self):
        pass

# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Creating instances
car = Car()
plane = Plane()
boat = Boat()

# Using the move method
for vehicle in (car, plane, boat):
    vehicle.move()
