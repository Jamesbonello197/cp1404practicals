"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
Values error occurs when the user inputs a string or float instead of an integer.

2. When will a ZeroDivisionError occur?
ZeroDivisionError will occur when a user inputs 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could add an if statement that says play if the denominator is 0, and ask the user for a valid input.

"""
# numerator = int(input("Enter the numerator: "))
# try:
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
# print("Finished.")

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero! Try again.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
