# Vehicle Management System

# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

# Subclass 1 - Car
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model} Fuel Type: {self.fuel_type}")

# Subclass 2 - Bike
class Bike(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity
    
    def display_info(self):
        print(f"Bike: {self.brand} {self.model} Engine: {self.engine_capacity}cc")

# Subclass 3 - Truck
class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity
    
    def display_info(self):
        print(f"Truck: {self.brand} {self.model} Load Capacity: {self.load_capacity} tons")

# Create vehicles
vehicles = [
    Car("Toyota", "Camry", "Petrol"),
    Car("Tesla", "Model 3", "Electric"),
    Bike("Honda", "CBR500R", 500),
    Bike("Royal Enfield", "Classic 350", 350),
    Truck("Volvo", "FH16", 40),
    Truck("Scania", "R450", 38)
]

# Display vehicle information
print("VEHICLE MANAGEMENT SYSTEM")
print("---------------------------------")
for vehicle in vehicles:
    vehicle.display_info()
