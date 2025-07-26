def add_student():
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    with open("students.txt", "a") as file:
        file.write(f"{name},{marks}\n")
    print(f"Student '{name}' added successfully!")

def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            if not students:
                print("No students found in the records.")
                return
                
            print("\nList of Students:")
            print("-----------------")
            for student in students:
                name, marks = student.strip().split(",")
                print(f"Name: {name}, Marks: {marks}")
            print("-----------------")
    except FileNotFoundError:
        print("No students found in the records.")

def remove_student():
    name_to_remove = input("Enter student name to remove: ")
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
        
        found = False
        with open("students.txt", "w") as file:
            for student in students:
                name, marks = student.strip().split(",")
                if name.lower() != name_to_remove.lower():
                    file.write(student)
                else:
                    found = True
            
        if found:
            print(f"Student '{name_to_remove}' removed successfully!")
        else:
            print(f"Student '{name_to_remove}' not found in records.")
    except FileNotFoundError:
        print("No students found in the records.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Remove Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()