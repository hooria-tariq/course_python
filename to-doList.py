Tasks = []  

while True:
    select = input("Enter 1 to Add Task, 2 to Remove Task, 3 to View Tasks and 4 to Exit : ")

    if select == "1":
        todo = input("Enter Task (or 'back' to return): ")
        if todo.lower() == "back":
            continue 
        Tasks.append(todo) 
        print(f"'{todo}' added successfully!")
    
    
    elif select == "2":
        todo = input("Enter Task to remove (or 'back' to return): ")
        if todo.lower() == "back":
            continue
        if todo in Tasks:
            Tasks.remove(todo)
            print(f"'{todo}' removed successfully!")
        else:
            print(f"'{todo}' not found in the list.")
    
    elif select == "3":
         print("\nList of Tasks:")
         for task in Tasks:
           print(f"- {task}")
    
    elif select == "4":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Try again.")