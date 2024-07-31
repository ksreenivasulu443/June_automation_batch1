# from abc import ABC, abstractmethod
#
#
# # Define an abstract class
# class Animal(ABC):
#
#     # Define an abstract method
#     @abstractmethod
#     def make_sound(self):
#         return "hello"
#     @abstractmethod
#     def make_sount2(self):
#         pass
#
#
# # Define a subclass that implements the abstract method
# class Dog(Animal):
#
#     def make_sound(self):
#         return "Woof"
#     def make_sount2(self):
#         pass
#
#
# # Define another subclass that implements the abstract method
# class Cat(Animal):
#
#     def make_sound(self):
#         return "Meow"
#     def make_sount2(self):
#         pass
#
#
# # Try to instantiate the abstract class (this will raise an error)
# #animal = Animal()
#
#
# # Instantiate the subclasses
# dog = Dog()
# cat = Cat()
#
# # Call the implemented methods
# print(dog.make_sound())  # Output: Woof
# print(cat.make_sound())  # Output: Meow


# class MyClass:
#     def __init__(self, value):
#         self.value = value  # Public attribute
#
#     def public_method(self):
#         return self.value  # Public method
#
# obj = MyClass(10)
# print(obj.value)  # Accessing public attribute
# print(obj.public_method())  # Accessing public method

# class MyClass:
#     def __init__(self, value):
#         self._value = value  # Protected attribute
#
#     def _protected_method(self):
#         return self._value  # Protected method
#
# obj = MyClass(20)
# print(obj._value)  # Accessing protected attribute (not recommended)
# print(obj._protected_method())  # Accessing protected method (not recommended)


class MyClass:
    def __init__(self, value):
        self.__value = value  # Private attribute

    def __private_method(self):
        return self.__value  # Private method

    def get_value(self):
        return self.__value  # Public method to access private attribute

obj = MyClass(30)
# print(obj.__value)  # AttributeError: 'MyClass' object has no attribute '__value'
# print(obj.__private_method())  # AttributeError: 'MyClass' object has no attribute '__private_method'
#
# # Accessing private attributes and methods indirectly
print(obj.get_value())









