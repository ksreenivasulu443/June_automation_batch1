from abc import ABC, abstractmethod


# Define an abstract class
class Animal(ABC):  # Animal is parent class and inheriting ABC class
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
    def new_method(self):
        print("new method")


class Dog(Animal): # child class must have parent abstract methods implementation
    def make_sound(self):
        print("make sound method")

    def move(self):
        print("move method")
    def new_method(self):
        print("new method")


class Cat(Animal): # child class must have parent abstract methods implementation
    def make_sound(self):
        print("make sound method")

    def move(self):
        print("this cat class move method")

obj = Animal()


#obj = Animal() # will fail beacuse Animal is abstract class


# obj = Dog()
#
# obj.make_sound()
# obj.move()
# obj.new_method()

obj2 = Cat()
obj2.move()
obj2.make_sound()

obj2.new_method()

obj3 = Cat()

# obj.Dog_sound()
# obj.make_sound()
