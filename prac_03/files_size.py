"""
Write a program that asks the user for a filename, then prints the number of lines in that file.

Use our standard while loop pattern to keep asking the user for filenames until they just press Enter (empty string)
Use a function to determine the file 'size' in number of lines. Follow SRP and consider what you should pass in and what you should return.
Use exceptions to handle missing files. This can be what we call "non-local catch". Even though you open the file inside your file-reading function, you want to handle the error in main().
Sample Output
Enter filename: no
ERROR: no does not exist.
Enter filename: no.py
ERROR: no.py does not exist.
Enter filename: readme.md
readme.md has 616 lines.
Enter filename:

"""


#
# print menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     else if choice == <second option>
#         <do second task>
#     ...
#     else if choice == <n-th option>
#         <do n-th task>
#     else
#         print invalid input error message
#     print menu
#     get choice
# <do final thing, if needed>


def main():
    while True:
        filename = input("Enter filename:").strip()
        if filename == "":
            break
        try:
            line_count = calculate_lines(filename)
            print(f"{filename} has {line_count} lines")
        except FileNotFoundError:
            print(f"Error: {filename} does not exist")


def calculate_lines(filename):
    number_of_lines = 0
    with open(filename, "r") as in_file:
        for line in in_file:
            number_of_lines += 1

    return number_of_lines


main()
