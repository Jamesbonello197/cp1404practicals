number_of_items = int(input("Enter number of items: "))
total_price = 0
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Enter number of items: "))

for n in range(1, number_of_items + 1):
    item_price = int(input(f"Price of item {n}: "))
    total_price += item_price
if total_price > 100:
    total_price = 0.9 * total_price
    print("You received a discount of 10% off!")
print(f"Total price for items {number_of_items} is ${total_price}")

