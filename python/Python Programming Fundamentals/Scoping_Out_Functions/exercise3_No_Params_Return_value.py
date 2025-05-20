# Begin by writing the function definition for a get_lucky_number function. Remember, this function should not require any input parameters (one line of code). Avoid type hints for the return value.
# The function should then return the value of lucky_num (one line of code). The value has already been loaded; your task is to return the value to the main program.
# Run the program. A random number will be generated in the range (1 to 100, as defined in the function). This allows the logic to be written once and re-used many times in the program.
import random
def get_lucky_number():
    lucky_num = random.randint(1,100)
    return lucky_num
lucky_number = get_lucky_number()
print("Your lucky number is:", lucky_number)