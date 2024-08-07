"""This module is created to practice Inheritance in python
Created on 30-07-2024"""

class Parent:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("constructor from Parent",a,b)

class Child(Parent):

    def __init__(self,name,a,b):
        super().__init__(22,33) #passing parameter for parent
        print("constructor from child",name)

obj = Child('darshan',11,22) #both parent & child constructor executed