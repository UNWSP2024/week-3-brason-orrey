#Brason Orrey - Package Shipping Calculator

weight = float(input("Please Enter the weight of your package: "))

if weight <= 2:
    price_per_pound = 1.50
elif weight > 2 and weight <= 6:
    price_per_pound = 3.00
elif weight > 6 and weight <= 10:
    price_per_pound = 4.00
else:
    price_per_pound = 4.75

total_shipping_cost = weight * price_per_pound

print(f"The total shipping charge is: ${total_shipping_cost:.2f}")
