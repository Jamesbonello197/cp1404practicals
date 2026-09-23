# write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
# The program should then print asterisks as long as the word.
# Example: if the user enters Pythonista (10 characters), the program should print **********.

""" """
from win32con import HELP_SETPOPUP_POS

MINIMUM_LENGTH = 8

password = input("Enter your password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password must be {MINIMUM_LENGTH} characters")
    password = input("Enter your password: ")

print(len(password) * "*")




