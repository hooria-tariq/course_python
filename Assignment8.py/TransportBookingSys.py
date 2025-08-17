#Transport Bookinf System


#base class

class Transport:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def book_ticket(self):
        print(f"Booking generic transport: {self.name} (Capacity: {self.capacity})")

#subclass 1

class Bus(Transport):
    def __init__(self, name, capacity, route_number):
        super().__init__(name, capacity)
        self.route_number = route_number
    
    def book_ticket(self):
        super().book_ticket()
        print(f"• Bus Route: {self.route_number}")

#subclass 2

class Train(Transport):
    def __init__(self, name, capacity, coach_type):
        super().__init__(name, capacity)
        self.coach_type = coach_type
    
    def book_ticket(self):
        super().book_ticket()
        print(f"• Coach Type: {self.coach_type}")

#subclass 3
class Flight(Transport):
    def __init__(self, name, capacity, airline):
        super().__init__(name, capacity)
        self.airline = airline
    
    def book_ticket(self):
        super().book_ticket()
        print(f"• Airline: {self.airline}")


# Create transport options
transports = [
    Bus("City Express", 50, 102),
    Train("Bullet Express", 300, "AC"),
    Flight("NYC-DXB", 350, "Emirates"),
    Bus("School Special", 40, 12),
    Train("Local Passenger", 500, "General"),
    Flight("LHR-JFK", 280, "British Airways")
]

print("Transport Booking System")
print("------------------------")
for transport in transports:
    transport.book_ticket()
    print()  