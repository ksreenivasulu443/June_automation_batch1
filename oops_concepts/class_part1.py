"""This module is created to practice OOPS Concepts in python
created by Chandan on 24-07-2024"""

#above is called as "Documentation String"

class Calc:
    pi = 3.14
    def __init__(self,a,b):
        self.a = a #this is instance variable
        self.b = b #this is instance variable

    def add(self):
        self.c = 100 #inside method creating instance variable
        return self.a + self.b + self.c

obj = Calc(11,22)

print(obj.a, obj.b) #Result --< 11 22
#here we can access the instance variables with in the class by using self variable
# & outside the class by using the object reference