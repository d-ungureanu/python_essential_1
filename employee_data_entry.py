# variable to capture number of employees as string
number_of_employees_str = input("Please enter the number of employees: ")
while not number_of_employees_str.isdigit():
    number_of_employees_str = input("Please enter a valid number of employees: ")

# var to save number of employees as integer
num_of_emp = int(number_of_employees_str)

# variable to save employees details
list_of_employees = {}

# variable to save the sum of all ages
sum_of_ages = 0

# loop to capture all employees details
for i in range(num_of_emp):
    # capture first name and check it is not empty
    first_name = input("Please enter the first name: ").strip().capitalize()
    while len(first_name) == 0:
        first_name = input("Please enter a valid first name: ").strip().capitalize()

    # capture last name and check it is not empty
    last_name = input("Please enter the last name: ").strip().capitalize()
    while len(last_name) == 0:
        last_name = input("Please enter a valid last name: ").strip().capitalize()

    # capture age, cast it to integer and check it is in 18 to 100 range
    age_str = input("Please enter the employee's age: ")
    while not age_str.isdigit():
        age_str = input("Please enter age as a number: ")
    age = int(age_str)
    while (age < 18) or (age > 100):
        age = int(input("Please enter an age in the 18 to 100 range: "))

    # add employees to dict using value of iterator as uniques key
    list_of_employees[i] = {"firstname": first_name, "lastname": last_name, "age": age}

    sum_of_ages += age

# format employees details print output
for entry in list_of_employees.values():
    print(f'{entry["firstname"]} {entry["lastname"]} is {entry["age"]} years old.')

# debug warning msg
# sum_of_ages=600

# check if sum of all ages is over 500
if sum_of_ages > 500:
    print("WARNING!!! The sum of all ages is over 500!!!")
