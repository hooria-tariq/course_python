import json
import os

def display_menu():
    print("JSON Book Manager")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Exit")

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    
    if title and author:
        books.append({"title": title, "author": author})
        print("Book added successfully!")
    else:
        print("Title and author cannot be empty!")

def view_books(books):
    if not books:
        print("No books in the library.")
        return
    
    print("Library Contents:")
    for book in books:
     print(f"{book['title']} by {book['author']}")

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():
    
    books = load_books()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add_book(books)
            save_books(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()