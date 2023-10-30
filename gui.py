
""" Imports Section """
import time
import backend

""" Functionality elements """
def clear_console():
    print('\n' * 40)


def press_to_proceed():
    input()


def choose_set():
    op = input(">")
    if op == '0':
        pass
    elif op == '1':
        arithmetic_op_screen()
    elif op == '2':
        conversion_set_screen()
    else:
        clear_console()
        print("Bad Input - Please select one of the two sets of algorithms")
        print("Press any button to go back to the main menu ...")
        press_to_proceed()
        main_gui()


""" Visual Elements """
def welcome_message():
    clear_console()
    print("Welcome to the Implementation of Conversions and Operations App")
    print("Press any button to proceed to the main menu ...")
    print('\n'*3)
    print("Made by Toni Hus")
    press_to_proceed()


def main_gui():
    clear_console()
    print("Please choose the algorithm set you want to access:")
    print()
    print("1. Arithmetic Operations - Addition, Subtraction, Multiplication or Division")
    print("2. Conversions between different bases")
    print("0. Exit the Application")
    print()
    choose_set()


def goodbye_screen():
    clear_console()
    print("Thank you for testing my app")
    print("Have a great day!")


def arithmetic_op_screen():
    clear_console()
    print("Enter the base of the numbers you want to perform operations with: ")
    base = int(input(">"))

    print()
    backend.arithmetic_operations(base)


def conversion_set_screen():
    clear_console()
    print()

    print("Enter the base of the number you want to convert: ")
    base = int(input(">"))
    print()

    ok = False
    number = 0
    while not ok:
        print("Please enter the number in base", base, "that you want to convert: ")
        number = int(input(">"))
        ok = backend.verify_number(number, base)
        if not ok:
            print("Bad Input - The number you have entered is not a correct representation in selected base")
            print()

    print()
    print("Enter the base you want to convert the number", number, "(which is written in base", base, ") to:")
    dest_base = int(input(">"))
    backend.conversion(number, base, dest_base)
