def numbers_sum(a, b):
    return a + b


def numbers_sub(a, b):
    return a - b


def numbers_div(a, b):
    if b != 0:
        return a / b


def numbers_mul(a, b):
    return a * b

def read_numbers():
    while True:
        first_number_str = input("Please enter the first number: ")
        if first_number_str.isdigit():
            first_number = int()


if __name__ == '__main__':
    print("this is main body")
