hot_dog_price = 3.50
chili_dog_price = 4.50

print("Choose a hot dog:")
print("1. Regular Hot Dog ($3.50)")
print("2. Chili Dog ($4.50)")
choice = int(input("Enter 1 for Regular Hot Dog or 2 for Chili Dog: "))

if choice == 1:
    price = hot_dog_price
    hot_dog_type = "Hot Dog"
elif choice == 2:
    price = chili_dog_price
    hot_dog_type = "Chili Dog"
else:
    print("Invalid choice.")

cheese_price = 0.50
peppers_price = 0.75
onions_price = 1.00

print("Would you like to add toppings? (Enter 'y' for yes, or 'n' for no)")

cheese = input("Add Cheese ($0.50)? ")
peppers = input("Add Peppers ($0.75)? ")
onions = input("Add Grilled Onions ($1.00)? ")

toppings_cost = 0

if cheese.lower() == 'y':
    toppings_cost += cheese_price
if peppers.lower() == 'y':
    toppings_cost += peppers_price
if onions.lower() == 'y':
    toppings_cost += onions_price

tax_rate = 0.07

subtotal = price + toppings_cost

tax = subtotal * tax_rate

total_cost = subtotal + tax

print()
print("Order Summary:")
print(f"Hot Dog Type: {hot_dog_type} - ${price:.2f}")
if toppings_cost > 0:
    print(f"Toppings: ${toppings_cost:.2f}")
else:
    print("No toppings added.")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
