"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    result = get_score_status()
    print(f"User score is: {result}")
    if result == "Excellent":
        print("You win a prize!")
    print(get_random_score_status())


def get_score_status() -> str:
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_random_score_status():
    random_score = random.randint(1, 100)
    print(f"Random : {random_score}", end=" = ")
    if random_score < 0 or random_score > 100:
        return "Invalid score"
    elif random_score >= 90:
        return "Excellent"
    elif random_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
