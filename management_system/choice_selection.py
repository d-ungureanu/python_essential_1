import employees_details


def select_option():
    while True:
        allowed_options = ["add", "rem", "mod", "id", "list", "size", "exit"]
        selection = input("""
Please choose your desired option:
'add' to add a user
'rem' to remove a user
'mod' to modify a user's details
'id' to display a specific user's details
'list' for the list of all users
'size' for the total number of employees
'exit' to exit the program
 Your choice is: """)
        if selection in allowed_options:
            if selection == "add":
                employees_details.add_employee()
            elif selection == "rem":
                employees_details.remove_employee()
            elif selection == "mod":
                employees_details.update_employee()
            elif selection == "list":
                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                for entry in employees_details.employees_db.keys():
                    print(employees_details.employees_db[entry])
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            elif selection == "size":
                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f"The database holds {len(employees_details.employees_db)} entries.")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            elif selection == "id":
                display_id = input("Please enter the ID you want to display: ")
                if display_id.isdigit() and int(display_id) in employees_details.employees_db.keys():
                    print(employees_details.employees_db[int(display_id)])
            elif selection == "exit":
                break

        else:
            print("\n _______________________________")
            print("| Please select a valid option. |")
            print(" _______________________________")
