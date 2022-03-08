def read_first_number():
    while True:
        first_number_str = input("Please enter the first number: ")
        if first_number_str.isdigit():
            first_number = int(first_number_str)
            return first_number
        else:
            print("Please enter a number.")


def read_second_number():
    while True:
        second_number_str = input("Please enter the second number: ")
        if second_number_str.isdigit():
            second_number = int(second_number_str)
            return second_number
        else:
            print("Please enter a number.")


def numbers_sum(a, b):
    return a + b


def numbers_sub(a, b):
    return a - b


def numbers_mul(a, b):
    return a * b


def numbers_div(a, b):
    return a / b


def numbers_op(op_sign, a, b):
    result = 0
    if op_sign == "+":
        result = numbers_sum(a, b)
    elif op_sign == "-":
        result = numbers_sub(a, b)
    elif op_sign == "*":
        result = numbers_mul(a, b)
    elif op_sign == "/":
        result = numbers_div(a, b)
    else:
        print("Unknown operation!")
    return result


def read_operation():
    allowed_operations = ["+", "-", "*", "/", "quit"]
    while True:
        operation = input("Please enter any of the following operations +, -, *, /, quit : ")
        if operation in allowed_operations:
            return operation
        else:
            print("Unknown operation.")


if __name__ == '__main__':
    op = ""
    while True:
        op = read_operation()
        if op.lower() == "quit":
            print("\nExiting calculator...")
            break
        num1 = read_first_number()
        num2 = read_second_number()
        if op == "/" and num2 == 0:
            print("Division by zero not possible!")
        else:
            print(f"{num1} {op} {num2} = {numbers_op(op, num1, num2)}")
