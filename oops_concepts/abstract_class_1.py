from abc import ABC, abstractmethod


# Define an abstract class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        """Abstract method that subclasses must implement"""
        pass

    def move(self):
        """Concrete method with implementation"""
        print("The animal moves")


# Define a subclass that implements the abstract method
class Dog(Animal):

    def make_sound(self):
        return "Woof"

    def move(self):
        """Optionally override the concrete method"""
        print("The dog runs")


# Define another subclass that implements the abstract method
class Cat(Animal):

    def make_sound(self):
        return "Meow"


    # This subclass does not override the move method
# Instantiate the subclasses

dog = Dog()
cat = Cat()

# Call the implemented methods
print(dog.make_sound())  # Output: Woof
dog.move()  # Output: The dog runs

print(cat.make_sound())  # Output: Meow
cat.move()  # Output: The animal moves (inherited from the abstract class)
