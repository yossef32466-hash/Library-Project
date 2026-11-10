from validation import name_validation, author_validation, year_validation
from data import *
def display_books(books):
    for dicti in books:
        print(dicti['name'], dicti["available"])

def get_book_name():
    book_name = input("Enter the book title: ").strip()
    return book_name

def search_book(books, name):
    for dicti in books:
        if dicti['name'] == name:
            print(dicti)
            break
    return None

def enter_the_book_details():
    print("Enter the book details by name, author and year!")
    
    while True:
        name = input("Enter the book name: ").strip()
        if name_validation(name) == False:
            print("Invalid name please try again ")
            continue
        break

    while True:
        author = input("Enter the book author: ").strip()
        if author_validation(author) == False:
            print("Invalid author please try again")
            continue
        break

    while True:
        try:
            year = int(input("Enter the book year: ").strip())
            if year_validation(year) == False:
                print("Invalid year please try again")
                continue
            
            break
        except:
            ValueError
            continue    
    while True:
        for dicti in books: 
            if dicti['name'] == name and dicti['author'] == author: 
                print("The book is available in the library.") 
                return None
         
        return {"id":len(books) ,"name":name, "author": author, "year": year, "available": True}

   

def add_book(book):
    books.append(book)
    print("הספר נוסף בהצלחה")

def input_book_id():
    while True:
        try:
            book_id = int(input("Enter the book id: ").strip())
            return book_id
        except ValueError:
            continue  

def check_book_id(book_id):
    while True:
        for dicti in books:
            if dicti["id"] == book_id:
                break
            else:
                print("The book is not in the library.")
                continue
        return dicti["available"] == True

def borrow_book(book_id):
    for dicti in books:
            if dicti["id"] == book_id:
                dicti["available"] = False
                break
     