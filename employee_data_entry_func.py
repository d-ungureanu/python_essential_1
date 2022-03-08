# define function to print dictionary of dictionaries
def print_dict(dictionary):
    for entry in dictionary.values():
        print(f'{entry["firstname"]} {entry["lastname"]} is {entry["age"]} years old.')


# function to capture first name and check it is not empty
def read_first_name():
    while True:
        first_name = input("Please enter the first name: ")
        if len(first_name.strip()) > 0:
            return first_name.capitalize()


# function to capture last name and check it is not empty
def read_last_name():
    while True:
        last_name = input("Please enter the last name: ")
        if len(last_name.strip()) > 0:
            return last_name.capitalize()


def read_age():
    while True:
        age_str = input("Please enter the age: ")
        if age_str.isdigit():
            age = int(age_str)
            if (age >= 18) and (age <= 100):
                return age
            else:
                print("Age should be between 18 and 100: ")
        else:
            print("Age should be a numeric input: ")


def read_employees_number():
    while True:
        employees_number_str = input("Please enter the number of employees: ")
        if employees_number_str.isdigit():
            employees_number = int(employees_number_str)
            if employees_number > 0:
                break
            else:
                print("Employees number should be greater than zero: ")
        else:
            print("Employees number should be a number: ")
    return employees_number


if __name__ == '__main__':
    emp_counter = read_employees_number()
    for employee_index in range(emp_counter):
        firstName = read_first_name()
        lastName = read_last_name()
        empAge = read_age()

        print(f"{firstName} {lastName} is {empAge} years old.")
