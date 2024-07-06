"""This file created to practise python complex type
and created by Sreeni on 25/Jun/2024"""

a = 1.5+1j #( 1.5 real value, 1 - imaginary value)
print("value of a is ", a)
print("type of a is ", type(a))
print("id of a is ", id(a))

b= 1.5 - 1j
print("value of b is ", b)
print("type of b is ", type(b))
print("id of b is ", id(b))

c= -5j
print("value of c",c)
print("type of c ",type(c))
print("id of c",id(c))

print("methods available on complex type value ", dir(a))

print("imaginary value of a", a.imag)

print("real value of a", a.real)

a = 5
print("value of a is ", a)
print("type of a is ", type(a))
print("id of a is ", id(a))
print("methods available on complex type value ", dir(a))
print("imaginary value of a", a.imag)




