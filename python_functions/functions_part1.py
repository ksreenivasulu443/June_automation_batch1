"""This module is created to practice functions in python
created by Chandan on 18-07-2024"""

#return
def cal(a,b):
    return a+b, a-b, a*b, a/b

sum, sub, mul, div = cal(11,22)
a = cal(11,22)
print(a) #results will be stored as tuple
print(sum, sub, mul, div) #indivisual results
