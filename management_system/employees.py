# File that handles employees details
employees_counter = 0


def read_firstname():
    while True:
        firstname = input("Please enter the first name: ").strip().capitalize()
        if firstname.isalnum() and len(firstname) > 1:
            break
        else:
            print("Please enter a valid name.")
    return firstname


def read_lastname():
    while True:
        lastname = input("Please enter the last name: ").strip().capitalize()
        if lastname.isalnum() and len(lastname) > 1:
            break
        else:
            print("Please enter a valid name.")
    return lastname


def read_birth_yeah():
    while True:
        birth_year_str = input("Please enter the year of birth (4 digits format): ")
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if (birth_year > 1900) and (birth_year < 2004):
                break
            else:
                print("Please enter a year between 1900 and 2004.")
        else:
            print("Please enter a 4 digits number.")
    return birth_year


def read_birth_month():
    while True:
        birth_month_str = input("Please enter the month of birth (1 to 12): ")
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month > 0) and (birth_month < 13):
                break
            else:
                print("Please enter a number between 1 and 12.")
        else:
            print("Please enter a number between 1 and 12.")
    return birth_month


def read_birth_day():
    while True:
        birth_day_str = input("Please enter the day of birth: ")
        if birth_day_str.isdigit():
            birth_day = int(birth_day_str)
            if (birth_day > 0) and (birth_day < 32):
                break
            else:
                print("Print enter a valid number for the day of birth.")
        else:
            print("Please enter a valid number as the day of birth.")
    return birth_day


def read_position():
    while True:
        position = input("Please enter the employment position: ")
        if position.isalnum() and len(position) > 1:
            break
        else:
            print("Please enter only letters and/or numbers, no special characters.")
    return position

