
""" Imports Section """
import time

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
    choose_set()


def arithmetic_op_screen():
    pass


def conversion_set_screen():
    pass
