"""This module is created to practice OOPS Concepts in python
created by Chandan on 24-07-2024"""

#above is called as "Documentation String"

class Calc:
    pi = 3.14
    def __init__(self,a,b):
        self.a = a #this is instance variable
        self.b = b #this is instance variable

    @staticmethod #this is static method, no class & instance variables
    def area_of_square(l,b): #here l & b are static variables
        return l*b

obj = Calc(11,22)
print(obj.area_of_square(111,222)) #l & b are static variables
