#School Member System

#base class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

#subclass 1
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def introduce(self):
        super().introduce()  
        print(f"I'm a student in grade {self.grade}.")

#subclass 2
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def introduce(self):
        super().introduce()  
        print(f"I teach {self.subject}.")

#subclass 3
class Staff(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role
    
    def introduce(self):
        super().introduce()  
        print(f"I work as {self.role} in the school.")


people = [
    Student("Ali", 12, 7),
    Teacher("Ayesha", 45, "Mathematics"),
    Staff("Saad", 52, "Librarian"),
    Student("Ayeza", 15, 10),
    Teacher("Saim", 38, "English Literature")
]

print("School Member Introductions")
print("----------------------------")
for person in people:
    person.introduce()
    print()  
    