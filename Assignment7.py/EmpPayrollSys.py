#Emplyee Payroll System 

class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    def calculate_salary(self):
        return self.base_salary

    def display(self):
        print(f'{self.name} - Base Salary: Rs.{self.base_salary}')

#sub class/ child class

class Manager(Employee):
    def __init__(self, name, base_salary,bonus):
        super().__init__(name, base_salary)
        self.bonus=bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

    def display(self):
        print(f'{self.name}(Manager) - Base Salary: Rs.{self.base_salary} Bonus: Rs{self.bonus} Total: Rs.{self.calculate_salary()}')


#sub class 2 

class Developer(Employee):
    def __init__(self, name, base_salary,overtime_hours,hourly_rate):
        super().__init__(name, base_salary)
        self.overtime_hours=overtime_hours
        self.hourly_rate=hourly_rate

    def calculate_salary(self):
        return self.base_salary + (self.overtime_hours * self.hourly_rate)

    def display(self):
        print(f'{self.name}(Developer) - Base Salary: Rs.{self.base_salary} Overtime Hours: {self.overtime_hours} Hourly Rate: Rs.{self.hourly_rate} Total: Rs.{self.calculate_salary()}')


#sub class 3 

class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name, stipend)

    def calculate_salary(self):
        return self.base_salary

    def display(self):
        print(f'{self.name}(Intern) - Stipend: Rs.{self.base_salary}')



employees=[
    Manager("Zara", 600000, 50000),
    Developer("Ali",540000, 6, 10000),
    Developer("Aleena", 480000, 5, 10000),
    Intern("Maya", 20000),
    Intern("Saif",30000)

]

print("\nEmployee Payroll")
print("---------------")
for employee in employees:
    employee.display()

print("\nSalary Summary:")
for employee in employees:
    print(f"{employee.name}: Rs.{employee.calculate_salary()}")

total = sum(employee.calculate_salary() for employee in employees)
print(f"\nTotal Payroll: Rs.{total}")