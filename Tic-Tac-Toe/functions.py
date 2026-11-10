from game_display import GAME_DISPLAY
from game_display import GAME_DISPLAY
def show_board():
    for row in GAME_DISPLAY:
        print(row)

def get_valid_input():
    while True:
        choice = input("Enter X or O:   ").lower().strip()
        if choice == 'x' or choice == 'o':
            return choice
        print("Invalid character, please enter again.")

def get_valid_location():
    while True:
        try:
            location = int(input("Enter the location by a number between 1 and 9:   ").strip())
            
        except ValueError: 
            print("Invalid number, please select again.") 
            continue
        if location > 0 and location < 10 :
            return location
        else:
            print("A number greater or smaller than what is permitted")
            continue
def check_whether_the_location_is_legal(choice, location):
    for i, row in enumerate(GAME_DISPLAY):
        for j, val in enumerate(row):
            if val == location:
                GAME_DISPLAY[i][j] = choice.upper() 
                return True
    return False



