# The starting code has a call to a function, happy_birthday, that you will be writing.
# Write the function definition for the function, happy_birthday, which takes two parameters, the first named age and the second named name (1 line of code). Avoid type hints for the parameters.
# The function should print Happy Birthday <name> and congratulations on turning <age> years old! to the user (1 line of code). For example, if you pass the values 22 for age and Nora for name, the program should display Happy Birthday Nora and congratulations on turning 22 years old! The function should not return a value. Ensure the spacing is consistent with the requirements (for example, "Happy Birthday  Nora" has two spaces between "Birthday" and "Nora" when it should have one).
# Run the program. As it is currently written, it will always display the same message, but it could be modified to accept input instead of always using the same values.
def happy_birthday(age:int, name:str):
    print(f"Happy Birthday", name,"and congratulations on turning", age, "years old!")

happy_birthday(22,"Nora")