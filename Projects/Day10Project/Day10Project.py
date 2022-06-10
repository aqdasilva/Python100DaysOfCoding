# calculator
from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiple(n1, n2):
    return n1 * n2


def divide(n1, n2):
    n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("what is the first number?: "))
    for symbol in operations:
        print(symbol)
    shouldContinue = True
    while shouldContinue:
        operationSymbol = input("pick an operation: ")
        num2 = float(input("what is the next number?: "))
        calculationFunction = operations[operationSymbol]
        answer = calculationFunction(num1, num2)
        print(f"{num1} {operationSymbol} {num2} = {answer}")

        if input(f"type 'y' to continue calculating with {answer}, or type 'n' to exit. ") == "y":
            num1 = answer
        else:
            shouldContinue = False
            calculator()


calculator()
