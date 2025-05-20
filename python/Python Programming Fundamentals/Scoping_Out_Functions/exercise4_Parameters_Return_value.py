# Begin by writing the function definition for the calc_sale_price function. This function will accept two input parameters (one line of code). The first, amount, is a number representing the amount of purchase. The second, member, is a boolean variable representing whether the user is a member (True) or not (False). Avoid type hints for the parameters and return type.
# Round amount to two decimal places using the built-in function round. Save the result in the amount variable.
# The function should then return the value of amount. 
# Run the code. The discounted amounts will be displayed.
def calc_sale_price(amount:float, member:bool):
    if member:
        amount = amount - (amount * 0.15)
    else:
        amount = amount - (amount * 0.05)
    amount = round(amount,2)
    return amount
full_price = 150.50
member_price = calc_sale_price(full_price, True)
print("Member price:",member_price)

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:",non_member_price)