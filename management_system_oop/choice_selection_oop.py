import employee_details_oop
import management_operations


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
                employee_details_oop.add_employee()
            elif selection == "rem":
                employee_details_oop.remove_employee()
            elif selection == "mod":
                employee_details_oop.update_employee()
            elif selection == "list":
                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                for entry in management_operations.employees_db.keys():
                    print(management_operations.employees_db[entry])
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            elif selection == "size":
                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f"The database holds {len(management_operations.employees_db)} entries.")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            elif selection == "id":
                display_id = input("Please enter the ID you want to display: ")
                if display_id.isdigit() and int(display_id) in management_operations.employees_db.keys():
                    print(management_operations.employees_db[int(display_id)])
            elif selection == "exit":
                break

        else:
            print("\n _______________________________")
            print("| Please select a valid option. |")
            print(" _______________________________")
