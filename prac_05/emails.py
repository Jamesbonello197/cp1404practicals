"""
estimate: 30min
actual : 35min
"""

email_to_name = {}


def extract_fullname(user_email):
    name_parts = user_email.split("@")[0].split(".")
    fullname = " ".join(name_parts).title()
    return fullname


def main():
    user_email = input("Email: ")
    while user_email != "":
        name = extract_fullname(user_email)
        user_confirmation = input(f"Is your name {name} (Y/N)").upper()

        if user_confirmation == "Y" or user_confirmation == "":
            email_to_name[user_email] = name
        else:
            name = input("Name: ")
            email_to_name[user_email] = name
        user_email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
