from game_display import GAME_DISPLAY
from functions import *

def nain():
    while True:
        show_board()
        choice = get_valid_input() 
        location = get_valid_location()
        check_whether_the_location_is_legal(choice, location)
        

if __name__ == "__main__":
    nain()