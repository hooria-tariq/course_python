students = []  

while True:
    select = input("Enter 1 to Add Student, 2 to Remove Student, 3 to View All and 4 to Exit : ")

    if select == "1":
        stu = input("Enter Student (or 'back' to return): ")
        if stu.lower() == "back":
            continue 
        students.append(stu) 
        print(f"'{stu}' added successfully!")
    
    
    elif select == "2":
        stu = input("Enter Student to remove (or 'back' to return): ")
        if stu.lower() == "back":
            continue
        if stu in students:
            students.remove(stu)
            print(f"'{stu}' removed successfully!")
        else:
            print(f"'{stu}' not found in the list.")
    
    elif select == "3":
         print("\nList of Students:")
         for student in students:
           print(f"- {student}")
    
    elif select == "4":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Try again.")