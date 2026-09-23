print("Enter your name:", end="")
name = input()

print("Select:\n(Q)uit\n(G)ood\n(H)ello)")
choice = input("")

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print(f"Invalid message")

    print("Select:\n(Q)uit\n(G)ood\n(H)ello)")
    choice = input("")
print("Finished message")

