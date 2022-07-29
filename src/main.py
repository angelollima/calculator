import os
from math import sqrt
from operator import add, sub, mul, pow

BOLD_TEXT = "\033[1m{:^60}\033[0m"

OPTIONS = """options:
+ for addition
- for subtraction
* for multiplication
** for exponentiation
/ for division
s for square root
ss for roots beyond square
c for clean
q to exit
:-> """


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "**": pow,
    "/": lambda x, y: x / y if y > 0 else "It can't be divided by zero",
    "s": lambda x: sqrt(x),
    "ss": lambda x, y: x ** (1/y) if y > 0 else "It can't be zero"
}


def main() -> None:
    print(BOLD_TEXT.format("Welcome to Easy Calculator"))

    while (operation := input(OPTIONS)) != "q":
        
        if operation == "c":
            os.system("clear" if os.name == "posix" else "cls")

        elif operation == "s":
            number = input("Enter one number: ")
            if not number.isnumeric():
                print(BOLD_TEXT.format("That's not a number!"))
                continue
            r = operations["s"](float(number))
            print(BOLD_TEXT.format(f"The square root of {number} is: {r:.2f}"))
        elif operation == "ss":
            rooting = input("Enter one number (rooting number): ")
            root_index = input("Enter the index of the square root: ")
            if not rooting.isnumeric() or not root_index.isnumeric():
                print(BOLD_TEXT.format("That's not a number!"))
                continue
            r = operations["ss"](float(rooting), float(root_index))
            print(BOLD_TEXT.format(f"The square root of {rooting} with index {root_index} is: {r:.2f}"))

        elif operation in operations:
            number_1 = input("Enter first number: ")
            number_2 = input("Enter second number: ")
            if not number_1.isnumeric() or not number_2.isnumeric():
                print(BOLD_TEXT.format("Both values ​​must be numbers!"))
                continue
            r = operations[operation](float(number_1), float(number_2))
            print(BOLD_TEXT.format(f"{number_1} {operation} {number_2} = {r}"))
        
        else:
            print(BOLD_TEXT.format(f"Hmm.. '{operation}' that's not an operation!"))
    print(BOLD_TEXT.format("Cya... Hope to see you soon"))

if __name__ == "__main__":
    main()