# Task 1: Database Schema Design

# Define the classes that represent the tables in the relational database.

class Author:
    # This class represents the Authors table.
    def __init__(self, author_id, name, bio):
        self.author_id = author_id  # Primary Key for Authors table
        self.name = name  # Name of the author
        self.bio = bio  # Short biography of the author

class Book:
    # This class represents the Books table.
    def __init__(self, book_id, title, author_id, genre, price, stock_quantity):
        self.book_id = book_id  # Primary Key for Books table
        self.title = title  # Title of the book
        self.author_id = author_id  # Foreign Key linking to the Authors table
        self.genre = genre  # Genre of the book
        self.price = price  # Price of the book
        self.stock_quantity = stock_quantity  # Quantity of the book in stock
        self.is_available = stock_quantity > 0  # Availability status of the book

    # Method to borrow a book (reduce stock)
    def borrow_book(self, quantity=1):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.is_available = self.stock_quantity > 0
            return True
        else:
            print(f"Not enough stock for book: {self.title}")
            return False

    # Method to return a book (increase stock)
    def return_book(self, quantity=1):
        self.stock_quantity += quantity
        self.is_available = True

class Customer:
    # This class represents the Customers table.
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id  
        self.name = name  
        self.email = email 
        self.phone = phone  

class Transaction:
    # This class represents the Transactions table.
    def __init__(self, transaction_id, customer_id, book_id, quantity, purchase_date, total_price):
        self.transaction_id = transaction_id  
        self.customer_id = customer_id  
        self.book_id = book_id 
        self.quantity = quantity 
        self.purchase_date = purchase_date  
        self.total_price = total_price  

# Task 2: Entity-Relationship Diagram (ERD) Creation

# Simulate the database with dictionaries that represent the tables.

# Authors table 
authors = {}

# Books table 
books = {}

# Customers table 
customers = {}

# Transactions table 
transactions = {}

# Add sample data to the simulated database
def add_sample_data():
    # Adding Authors 
    author1 = Author(1, "Shanteek Love", "Indian author, best known for her heart warming ways of writing.")
    author2 = Author(2, "Anthony Milton", "American novelist and short-story writer, best known for his unique way of keeping the reader engaged.")
    authors[author1.author_id] = author1
    authors[author2.author_id] = author2

    # Adding Books 
    book1 = Book(1, "The Way Of Love", 1, "Romance", 39.99, 50)
    book2 = Book(2, "If You Think It", 2, "Reality", 49.99, 30)
    books[book1.book_id] = book1
    books[book2.book_id] = book2

    # Adding Customers 
    customer1 = Customer(1, "Terrell Heard", "heard@gmail.com", "745-1234")
    customer2 = Customer(2, "Alante Milton", "milton@yahoo.com", "968-5678")
    customers[customer1.customer_id] = customer1
    customers[customer2.customer_id] = customer2

    # Adding Transactions 
    transaction1 = Transaction(1, 1, 1, 2, "2024-08-22", 79.98)
    transaction2 = Transaction(2, 2, 2, 1, "2024-08-22", 49.99)
    transactions[transaction1.transaction_id] = transaction1
    transactions[transaction2.transaction_id] = transaction2

# Display data functions to visualize the data in the "tables"

def display_books():
    # Display all books and their details (Task 2: ERD - Books Table)
    print("Books in BookHaven:")
    for book in books.values():
        availability = "Available" if book.is_available else "Unavailable"
        print(f"{book.title} by {authors[book.author_id].name}, Genre: {book.genre}, Price: ${book.price}, Stock: {book.stock_quantity}, Status: {availability}")

def display_customers():
    # Display all customers and their details (Task 2: ERD - Customers Table)
    print("Customers:")
    for customer in customers.values():
        print(f"ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

def display_transactions():
    # Display all transactions and their details (Task 2: ERD - Transactions Table)
    print("Transactions:")
    for transaction in transactions.values():
        print(f"Transaction ID: {transaction.transaction_id}, Customer: {customers[transaction.customer_id].name}, Book: {books[transaction.book_id].title}, Quantity: {transaction.quantity}, Total Price: ${transaction.total_price}, Date: {transaction.purchase_date}")

# Example usage to see how the database works

add_sample_data()  # Populate the database with sample data
display_books()    # Show all books in the store
display_customers()  # Show all customers
display_transactions()  # Show all transactions