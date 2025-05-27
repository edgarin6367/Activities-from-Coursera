# Write a Python function named read_file_contents that takes file_path as an argument.
# Inside the function, use a try-except block to attempt to open the file, read its contents, and print them to the console.
# Handle the FileNotFoundError specifically by printing an appropriate error message if the file doesn't exist.
# Write your Python program below
file_name =  "shopping_cart.txt"
def read_file_contents(file_path):
    """Reads the contents of a file and prints them to the console."""
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print (f"Error: File not found - {file_path}")
read_file_contents("/Users/Example/Documents/my_file.txt")