def input_validation(in_user):
    try:
        input_user = in_user.strip()
        valid_input = int(input_user)
        if valid_input < 1 or valid_input > 8:
            print("The selection must be a number Between 1 and 8")
            return False
        return valid_input
    except ValueError:
        print("The selection must be a number from the menu.")
        return False


def name_validation(name):
    if not isinstance(name, str):
        print("Name must be a string")
        return False
    return True

def author_validation(author):
    if not isinstance(author, str):
        print("Author must be a string")
        return False
    return True

def year_validation(year):
    print(type(year))
    if not isinstance(year, int) or year < 1:
        print(type(year))
        print("Year must be a positive number")
        return False
    return True



