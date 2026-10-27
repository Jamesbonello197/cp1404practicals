# Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that
# many lines of output. Each line consists of 6 random numbers between 1 and 45. These values should be stored as
# CONSTANTS.
#
# Each line (quick pick) should not contain any repeated number.
# Each line of numbers should be displayed in sorted (ascending) order.
# Study the formatting below so that numbers align neatly.
# Note
#
# Your code should produce output that matches this sample output (except the numbers are random):
#
# How many quick picks? 5
#  1 12 14 15 30 36
#  2  5  8 33 38 41
#  2 12 19 22 29 43
# 13 21 28 29 42 43
#  3  4 10 11 32 44
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6

number_of_picks = int(input("How many quick picks?"))
for number in range(number_of_picks):
    quick_picks = []
    while len(quick_picks) < number_of_picks:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_picks:
            quick_picks.append(number)

    print(" ".join(f"{num:2}" for num in sorted(quick_picks)))

# quick_picks.sort()
#print(" ".join(f"{num:2}" for num in quick_picks)) we will use this