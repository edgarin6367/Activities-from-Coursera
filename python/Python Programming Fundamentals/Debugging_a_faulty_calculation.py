def calculate_discount(price, discount_percentage):
  discount_amount = price * (discount_percentage / 100)
    # discounted_price = price + discount_amount # incorrect line
  discounted_price = price - discount_amount # corrected line

  return discounted_price


# Code to test your output
price = 50
discount_percentage = 20
discounted_price = calculate_discount(price, discount_percentage)
print(discounted_price)