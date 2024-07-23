"""This module is created to practice name space in python
created by Chandan on 23-07-2024"""

#global space #this is accessed by anywhere in the program
a = 100
b = 20

def out_fun(): #enclosing space #this will be accessed by both enclosing & local space
    global a,c
    a = 24
    c = 21
    print("global variables for out_fun are:",globals()) #24, 20 & 21 are globals #global a is over written
    print("local variables for out_fun are:", locals()) # No Locals

    def inner_fun(): #local space #this is accessed by only local space
        d = 45
        print("global variables for inner_fun are:", globals())  # 24, 20 & 21 are globals
        print("local variables for inner_fun are:", locals())  # 45 is locals
    inner_fun()
out_fun()

for i in range(1,10):
    print(i/0, end=" ")
else:
    print("else block:",i)
