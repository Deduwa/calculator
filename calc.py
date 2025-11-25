def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

start_again = True
while start_again:
    first_number = float(input("Input first number\n"))
    op_symbol = input("Choose a operation\n + \n - \n * \n / \n")
    operation = operations[op_symbol]
    second_number = float(input("Input second number\n"))
    result = operation(first_number, second_number)
    print(f"{first_number} {op_symbol} {second_number} is equal to {result}")
    continue_calculation = True
    while continue_calculation:
        answer = input(
            "To continue calculating with the result type yes\nTo start over type again\nTo exit the calculator type quit\n").lower()
        if answer == "yes":
            first_number = result
            op_symbol = input("Choose a operation\n + \n - \n * \n / \n")
            operation = operations[op_symbol]
            second_number = float(input("Input second number\n"))
            result = operation(first_number, second_number)
            print(f"{first_number} {op_symbol} {second_number} is equal to {result}")
        elif answer == "again":
            print("\n" * 100)
            continue_calculation = False
        elif answer == "quit":
            continue_calculation = False
            start_again = False
