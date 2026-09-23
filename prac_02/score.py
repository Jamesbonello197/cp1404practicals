"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

MENU = """(G)et a valid score (must be 0-100)
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "G":
            get_score_status()
        elif choice == "P":
            result = get_score_status()
            print(f"User score is: {result}")
        elif choice == "S":
            score = float(input("Enter score: "))
            print(int(score) * "*")
        else:
            print("Invalid")
        print(MENU)
        choice = input().upper()


def get_score_status():
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
