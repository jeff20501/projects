#Library Catalog
class Book:
    def __init__(self, author, ISBN, available = True):
        self.author = author
        self.ISBN = ISBN
        self.available = available
        
class Library:
    def __init__(self):
        self.books = {
            'the road' : Book('jeff', 22344, available= True)
        }
     
    def add_a_book(self, new_book, author, ISBN):
        self.books[new_book] = Book(author, ISBN)
        print(f"The book with the title {new_book} by the Author {author} with ISBN {ISBN} has been successfully added!")
        
    def remove_a_book(self, old_book):
        if old_book in self.books:
            del self.books[old_book]
            print(f"The book with the title {old_book} was successfully removed from the library!")
        else:
            print(f"The book with the title {old_book} was not located in the library!")
    
    def borrow_a_book(self, title):
        if title in self.books: # this checks if the book title given is in the library
            if self.books[title].available: # This checks if the book is available or not
                self.books[title].available = False 
                # If the book's bool is True (available) this code runs and then the availability of the book is changed to False
                print(f"The book with the title {title} was successfully borrowed.")
            
            else:
                print(f"The book with the title {title} is currently not available.")
                
        else:
            print(f"The book with the title {title} is not in the library!")
            
    def return_a_book(self, title):
        if title in self.books:
            if self.books[title].available: # If the book is available then the following code will run
                print(f"This book with the title {title} was never borrowed!")
            else:
                self.books[title].available = True # If the book's bool was false the the following code will run
                print(f"The book with the title {title} has been successfully returned!")
        else:
            print(f"This book with the title {title} is not in the library!")
                
    def list_all_books(self):
        if not self.books:
            print("This library has no books!")
        else:
            print("This is a list of all the Library books:")
            for title, book in self.books.items(): 
                # This loop loops over the dict self.books the title is the key and the book is the value of the key which are author, ISBN and available
                print(f"{title} by {book.author}, ISBN:{book.ISBN}, available:{book.available}")
                print()


print(f"Welcome to our library")
library = Library()

while True:
    
    print("The following are services offered:")
    
    print("1. Add a book.")
    print("2. Remove a book.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. List all the books.")
    print("6. Exit.")
    
    choice = int(input("What service do you want to be offered: "))
    
    if choice == 1:
        new_book = input("Enter the title of book you want added: ")
        author = input("Enter the Author\'s name: ")
        ISBN = input("Enter the book number (ISBN) of the book: ")
        library.add_a_book(new_book, author, ISBN)
    
    elif choice == 2:
        print("Are you sure you want to continue. If you wish to continue type in '1' if otherwise type in '0'.")
        choice2 = int(input("What is your choice:"))
        if choice == 1:
            old_book = input("Enter the title of the book you want removed.")
            library.remove_a_book(old_book)
        
        else:
            print("Have a nice day goodbye!")
    
    elif choice == 3:
        title = input("Enter the title of the book you want to borrow:")
        library.borrow_a_book(title)
    
    elif choice == 4:
        title = input("Enter the title of the book you want to return:")
        library.return_a_book(title)
    
    elif choice == 5:
        library.list_all_books()
    
    elif choice == 6:
        print("Thank you for using our services have a nice day.")
        
        break
        