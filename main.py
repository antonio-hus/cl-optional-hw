# Optional Homework in Computational Logic - Implementation of Conversions and Operations
# Made by Toni Hus

""" Imports Section """
import gui
import backend


def start():
    print(backend.base10_successive_divisions_method(10, 2))
    gui.welcome_message()
    gui.main_gui()
    gui.goodbye_screen()


start()

