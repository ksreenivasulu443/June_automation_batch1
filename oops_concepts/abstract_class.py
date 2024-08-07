"""This module is created to practice abstract class in python
created by chandan on 31-07-2024"""

from abc import ABC, abstractmethod #this is mandatory for abstract class

class Animal(ABC): #Animal is parent class & inheriting ABC Class

    @abstractmethod #this is decorators
    def make_sound(self):
        """Abstract method that subclasses must implement"""
        pass

    def move(self):
        """Abstract method that subclasses must implement"""
        pass

class Dog(Animal):

    def Dog_sound(self):
        print("this is Dog Sound method")

    def make_sound(self):
        print("make sound method")

#obj = Animal() #this fail because Animal is abstract class

obj = Dog()
obj.Dog_sound()
obj.make_sound()

