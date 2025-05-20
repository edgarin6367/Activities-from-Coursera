# You have created a file named menus.py stored in the same folder as your current program. This module contains a function, display_menu, that has been written. It takes no arguments and returns a numeric value.
# Import the menus module to make the contents available to your program.
# Enter the code to call the display_menu module in the menus module. The result will be saved in the user_choice variable.
# This code requires a menus.py file. It will work on the Coursera platform, but it would not work in a separate code editor on your system. Designing this way allows another programmer to modify the menus module independently of your code, and your program will benefit from the latest update.
import menus

# Call the display_menu function in the menus module
user_choice = menus.display_menu()

print(user_choice)