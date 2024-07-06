"""This file created to practise python boolean type
and created by Sreeni on 25/Jun/2024"""

a = True
print("value of a is ", a)
print("type of a is ", type(a))
print("id of a is ", id(a))
b = True
print("value of b is ", b)
print("type of b is ", type(b))
print("id of b is ", id(b))

c = False
print("value of c is ", c)
print("type of c is ", type(c))
print("id of c is ", id(c))

d = False
print("value of d is ", d)
print("type of d is ", type(d))
print("id of d is ", id(d))
#
print("methods available on boolean", dir(a))

# True - 1
# False - 0

print("__add__ on a and c value", d.__add__(c))

# int, float, bool
#
# source_count = 10
# percentage_fail = 20.3
# is_fail = True