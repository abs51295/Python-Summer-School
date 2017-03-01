class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def stand(self):
        """Simulate a dog standing"""
        print(self.name.title() + " is now standing")


my_dog = Dog("Tommy", 15)
print("My dog's name is: " + my_dog.name.title())
print("My dog's age is: " + str(my_dog.age))

my_dog.sit()
my_dog.stand()
