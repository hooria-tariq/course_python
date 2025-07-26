def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Goodbye! ")
            break
        else:
            print("Invalid choice. Please try again.")

def add_expense():
    """Add a new expense to the file"""
    print("Add New Expense")
    item = input("Enter item name: ")
    
    while True:
        amount = input("Enter amount: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    with open("expenses.txt", "a") as file:
        file.write(f"{item},{amount}\n")
    print("Expense added successfully!")

def view_expenses():
    """Display all expenses in a formatted table"""
    print("All Expenses")
    print("-" * 30)
    print(f"{'Item':<20} {'Amount':>8}")
    print("-" * 30)
    
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            
            if not expenses:
                print("No expenses recorded yet.")
                return
                
            for expense in expenses:
                item, amount = expense.strip().split(",")
                print(f"{item:<20} ${float(amount):>7.2f}")
                
    except FileNotFoundError:
        print("No expenses recorded yet.")

def calculate_total():
    """Calculate and display the total amount spent"""
    total = 0.0
    
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            
            if not expenses:
                print("No expenses recorded yet.")
                return
                
            for expense in expenses:
                _, amount = expense.strip().split(",")
                total += float(amount)
                
        print(f"\n💰 Total Amount Spent: ${total:.2f}")
        
    except FileNotFoundError:
        print("No expenses recorded yet.")

main()