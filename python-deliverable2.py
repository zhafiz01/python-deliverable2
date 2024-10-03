print("Welcome to the Fruit Market!")

name = input("What is your name?\n")
print(f"Welcome, {name}!")

apple_price = 2
grape_price = 1
orange_price = 3

apple_count = 0
grape_count = 0
orange_count = 0

while True:

    print("\nWhich fruit would you like to buy?")
    print("1. Apple - $2")
    print("2. Grape - $1")
    print("3. Orange - $3")

    choice = input("> ")

    if choice == "1":
        apple_count += 1
        print("You bought 1 apple.")
    elif choice == "2":
        grape_count += 1
        print("You bought 1 grape.")
    elif choice == "3":
        orange_count += 1
        print("You bought 1 orange.")
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        continue


    another = input("Would you like to buy another piece of fruit? (y/n)\n> ").lower()
    if another != 'y':
        break


subtotal = (apple_count * apple_price) + (grape_count * grape_price) + (orange_count * orange_price)
tax = subtotal * 0.05
total = subtotal + tax


print(f"\nReceipt for {name}")
print(f"{apple_count} apple(s) at ${apple_price} each")
print(f"{grape_count} grape(s) at ${grape_price} each")
print(f"{orange_count} orange(s) at ${orange_price} each")
print(f"Sub Total: ${subtotal}")
print(f"5% Tax: ${tax}")
print(f"Total: ${total}")

