from print_for_users import menu_printing
from validation import input_validation
from functions import display_books, get_book_auther, search_book_bt_author, get_available_books, return_book, borrow_book, check_book_id, input_book_id, get_book_name, search_book, enter_the_book_details, add_book
from data import books
def show_menu_and_get_selection():
    user_input = ""
    while user_input!="8":
        user_input = menu_printing()
        valid_input = input_validation(user_input)

        if valid_input == False:
            show_menu_and_get_selection()


        if valid_input == 1:
            display_books(books)
            show_menu_and_get_selection()
        if valid_input == 2:
            name = get_book_name()
            search_book(books, name) 

        if valid_input == 3:
            book = enter_the_book_details()
            add_book(book)

        if valid_input == 4:
            book_id = input_book_id()
            check_book_id(book_id)
            borrow_book(book_id)

        if valid_input == 5:
            book_id = input_book_id()
            book_id = check_book_id(book_id)
            return_book(book_id)
        
        
        if valid_input == 6:
            get_available_books()

        if valid_input == 7:
            book_auther = get_book_auther()
            search_book_bt_author(book_auther)


        if valid_input == 8:
            break















if __name__ == "__main__":
    show_menu_and_get_selection()