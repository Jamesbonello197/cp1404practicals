"""
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
"""
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print( "-----  Menu  -----\nSelect:\n(1) Show the even number of x to y\n(2) Show the odd number from x to y\n(3) Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)\n(4) Exit the program")
choice = int(input())

while choice != 4 and choice != 3 and choice != 2 and choice != 1:
    print("Invalid choice, try again")
    print("---Menu---\nSelect:\n(1) Show the even number of x to y\n(2) Show the odd number from x to y\n(3) Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)\n(4) Exit the program")
    choice = int(input())

if choice == 1:
    if x % 2 != 0:
        start = x + 1
    else:
        start = x
    for i in range(start, y + 1, 2):
        print(i, end=" ")
    print()
elif choice == 2:
    if x % 2 == 0:
        start = x + 1
    else:
        start = x
    for i in range(start, y + 1, 2):
        print(i, end=" ")
    print()
elif choice == 3:
    for i in range(x, y + 1):
        print(i ** 2, end=" ")
else:
    print("Goodbye")
