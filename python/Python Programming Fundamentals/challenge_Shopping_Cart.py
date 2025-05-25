# Create a list named shopping_cart to store the items as it allows for easy addition and removal of items.

# Add the following items to the list using three separate append methods:
# apple
# banana
# milk

# Note: This could also be done with the extend method, but this example is focusing on the more common append method.

# Use a for loop to iterate through each item in the shopping_cart list and print each item. Ensure you use the variable name item for each item in the list.

shopping_cart = []
shopping_cart.append("apple")
shopping_cart.append("banana")
shopping_cart.append("milk")
print("Shopping Cart:")
for item in shopping_cart:
    print(item)