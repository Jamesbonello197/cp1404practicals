# write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
# The program should then print asterisks as long as the word.
# Example: if the user enters Pythonista (10 characters), the program should print **********.

""" """


MINIMUM_LENGTH = 8


def main():
    password = get_valid_password()
    print_stars(password)


def print_stars(password: str):
    print(len(password) * "*")


def get_valid_password() -> str:
    password = input("Enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be {MINIMUM_LENGTH} characters")
        password = input("Enter your password: ")
    return password


main()
