
item = input("Enter an item: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity: "))
total_cost = price * quantity
print(f"The total cost for {quantity} {item}(s) is: ${total_cost:.2f}")