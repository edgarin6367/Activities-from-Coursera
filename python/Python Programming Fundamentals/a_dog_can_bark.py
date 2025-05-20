# Create a Python class named Dog.
class dog:    
# Define two attributes within the Dog class: name (a string to store the dog's name) and breed (a string to store the dog's breed).
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
# Implement a method named bark() within the Dog class. This method should print a message to the console that includes the dog's name and breed:
    def bark(self):
        print("Woof! My name is ", name, "and I'm a ", breed)
# Woof! My name is name and I'm a breed.
# Verify the period appears at the end of the printout.

# (provided) Create an instance (object) of the Dog class, name it my_dog. As this is not part of the Dog class, it will not be indented. 

# (provided) Using the my_dog variable instance. call the bark() method, providing the name Buddy and the breed Golden Retriever to see it in action!