emp_list = {
    1: {"name": "daniel",
        "surname": "ungureanu"},
    2: {
        "name": "mihai",
        "surname": "tolea"
    }
}
txt = "surname"
print(emp_list[1])
print(emp_list[2])

emp_list[1]["name"] = "Mihai"
emp_list[1][txt] = "Popescu"

print(emp_list[1])