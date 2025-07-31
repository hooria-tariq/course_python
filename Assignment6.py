# ---> Q1 : CLASS AND OBJECT CREATION 

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
Car1= Car("Hyundai","Elantra",2024)
Car2= Car("Kia","Sportage",2023)

print(f"---------Car 1 details----------\nBrand : {Car1.brand}\nModel : {Car1.model}\nYear : {Car1.year}\n")
print(f"---------Car 2 details----------\nBrand : {Car2.brand}\nModel : {Car2.model}\nYear : {Car2.year}\n")

print(f"\n")

# ---> Q2 : USE OF SELF AND INSTANCE VARIABLE

class Car:
    def __init__(self,car,brand,model,year):
        self.car=car
        self.brand = brand
        self.model = model
        self.year = year
    
    def displayinfo(self):
        print(f"------------{self.car} Details---------\nBrand : {self.brand}\nModel : {self.model}\nYear : {self.year}\n")

Car1= Car("Car 1","Hyundai","Elantra",2024)
Car2= Car("Car 2","Kia","Sportage",2023)

Car1.displayinfo()
Car2.displayinfo()

print(f"\n")

# ---> Q3 : CLASS VS INSTANCE VARIABLES

class Student:
    school_name = "ABC High School"  
    
    def __init__(self, name, grade):
        self.name = name      
        self.grade = grade   
student1 = Student("Ali", 10)
student2 = Student("Babar", 11)

# Printing school name 
print(student1.school_name)
print(student2.school_name)  
print(Student.school_name)   

# Changing school name
Student.school_name = "XYZ High School"
print(student1.school_name)  

print(f"\n")

# ---> Q4 : CONSTRUCTOR AND INITIALIZATION 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

Person1= Person("Sara",20)
Person2= Person("Maria",18)

Person1.introduce()
Person2.introduce()

print(f"\n")

# ---> Q5 : INHERITANCE BASICS

class Animal:
    def make_sound(self):
        print("Animals make sound")

class Dog(Animal): 
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")     

animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()  
dog.make_sound()     
cat.make_sound()   

print(f"\n")

# ---> Q6 : USING SUPER()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  
        self.department = department

manager = Manager("Aleeza", 90000, "CS")

print(f"Manager : {manager.name}\nSalary : Rs.{manager.salary}\nDepartment : {manager.department}\n")

print(f"\n")

# ---> Q7 : CONSTRUCTOR CHAINING WITH INHERITANCE

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, engine_cc):
        super().__init__(brand) 
        self.engine_cc = engine_cc
    
    def display(self):
        print(f"Brand: {self.brand}\nEngine: {self.engine_cc}cc")

bike = Bike("Honda", 150)
bike.display()

print(f"\n")

# ---> Q8 : COUNT NUMBER OF OBJECTS

class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1  

for i in range(5):
    c = Counter()

print(f"Total objects created: {Counter.count}")  

print(f"\n")

# ---> Q9 : INHERITANCE WITH POLYMORPHISM

class Shape:
    def area(self):
        pass  

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)

shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(f"Area: {shape.area()}")