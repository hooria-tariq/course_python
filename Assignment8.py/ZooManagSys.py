#Zoo Management System

#Base class

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"{self.name} the {self.species} makes a sound.")

#subclass 1

class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span
    
    def make_sound(self):
        print(f"{self.name} the {self.species} chirps melodiously! (Wingspan: {self.wing_span}cm)")

#subclass 2

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color
    
    def make_sound(self):
        print(f"{self.name} the {self.species} growls loudly! (Fur color: {self.fur_color})")

#subclass 3

class Reptile(Animal):
    def __init__(self, name, species, is_venomous):
        super().__init__(name, species)
        self.is_venomous = is_venomous
    
    def make_sound(self):
        venom_info = "venomous" if self.is_venomous else "non-venomous"
        print(f"{self.name} the {self.species} hisses! ({venom_info})")


# Create some animals
zoo = [
    Bird("Sky", "Eagle", 200),
    Mammal("Leo", "Lion", "Golden"),
    Reptile("Slither", "Cobra", True),
    Bird("Tweety", "Canary", 25),
    Mammal("Baloo", "Bear", "Brown"),
    Reptile("Crush", "Turtle", False)
]

print("Zoo Animal Sounds")
print("-----------------")
for animal in zoo:
    animal.make_sound()
    print()