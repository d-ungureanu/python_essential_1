# File that handles employees details
employees_counter = 0
# employees_db = {}
employees_db = {
    1: {
        "firstname": "Daniel",
        "lastname": "Ungureanu",
        "day": 21,
        "month": 3,
        "year": 1988,
        "position": "Support",
        "graduated": True,
        "id": 1
    },
    2: {
        "firstname": "John",
        "lastname": "Doe",
        "day": 11,
        "month": 1,
        "year": 1984,
        "position": "Listener",
        "graduated": False,
        "id": 2
    },
    3: {
        "firstname": "Jane",
        "lastname": "Doe",
        "day": 31,
        "month": 6,
        "year": 1991,
        "position": "Spender",
        "graduated": True,
        "id": 3
    }
}


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
        position = input("Please enter the employment position: ").strip()
        if len(position) > 1:
            break
        else:
            print("Please enter more than one character.")
    return position


def read_graduation():
    while True:
        graduation_str = input("""Has the employee graduated from university?
('y' for yes, 'n' for no): """).strip()
        if graduation_str == "y":
            graduation = True
            break
        elif graduation_str == "n":
            graduation = False
            break
        else:
            print("Please enter one of the correct options.")
    return graduation


def read_employee_details():
    global employees_counter
    employees_counter += 1
    firstname = read_firstname()
    lastname = read_lastname()
    dob_day = read_birth_day()
    dob_month = read_birth_month()
    dob_year = read_birth_yeah()
    position = read_position()
    grad = read_graduation()
    employee = {
        "firstname": firstname,
        "lastname": lastname,
        "day": dob_day,
        "month": dob_month,
        "year": dob_year,
        "position": position,
        "graduated": grad,
        "id": employees_counter
    }
    return employee


def add_employee():
    global employees_db
    global employees_counter
    employee = read_employee_details()
    employees_db[employees_counter] = employee
    print(" __________________________________________________________________")
    print("| Employee added successfully, to check database use 'list' option. |")
    print(" __________________________________________________________________")


def remove_employee():
    global employees_db
    rem_id_str = input("Please enter the ID you want to remove from database: ").strip()
    if rem_id_str.isdigit() and int(rem_id_str) in employees_db:
        rem_id = int(rem_id_str)
        del employees_db[int(rem_id)]
        print("\n _______________________________________________________")
        print(f"Employee with ID {rem_id} has been removed from database.")
        print(" _______________________________________________________")


def update_employee():
    global employees_db
    mod_id_str = input("Please enter the ID you want to update: ").strip()
    if mod_id_str.isdigit() and int(mod_id_str) in employees_db:
        print("ID found in database, please select field you want to update:")
        mod_option = input("""
 _______________________________________
| 1 - First Name                        |
| 2 - Last Name                         |
| 3 - Day of Birth                      |
| 4 - Month of Birth                    |
| 5 - Year of Birth                     |
| 6 - Employment Position               |
| 7 - Graduation status                 |
 _______________________________________
 Your choice is: """)
        mod_id = int(mod_id_str)
        if mod_option == "1":
            mod_str = "firstname"
            mod_data = read_firstname()
        elif mod_option == "2":
            mod_str = "lastname"
            mod_data = read_lastname()
        elif mod_option == "3":
            mod_str = "day"
            mod_data = read_birth_day()
        elif mod_option == "4":
            mod_str = "month"
            mod_data = read_birth_month()
        elif mod_option == "5":
            mod_str = "year"
            mod_data = read_birth_yeah()
        elif mod_option == "6":
            mod_str = "position"
            mod_data = read_position()
        elif mod_option == "7":
            mod_str = "graduated"
            mod_data = read_graduation()
        employees_db[mod_id][mod_str] = mod_data
        print("____________________________________________________________________________")
        print(f"Field {mod_str} for entry with ID: {mod_id}, had been changed to {mod_data}.")
        print("____________________________________________________________________________")
