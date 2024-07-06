"""This module file is create to practice python operators
created by Sreeni on 07/05/2024 """

a = 5

x = y = z = 10

# x=10
# y=10
# z=10

print("x value", x)
print("y value", y)
print("z value", z)
print("id of x,y,z", id(x), id(y), id(z))

k, l, m = 10, 20, 30

print("k value", k)
print("l value", l)
print("m value", m)
print("id of k,l,m", id(k), id(l), id(m))

sum1 = k + l + m - x * 5

print("sum1", sum1)

p = 10

p += 5  # p= p+5

print("p value ", p)

p -= 6  # p = p-6

print("p value ", p)
p *= 2  # p = P*2
print("p value is", p)
p /= 3
print("p value is", p)

p = +3

print("p value is", p)
k = 10
k = 4

print("2 ** 4", 2 ** 5)

a = 3
b = 2
print("a**b", a ** b)
a **= a  # a = a**a
print("a value ", a)
x, y, z = 10, 20, -2
print("x value", x)
print("y value", y)
print("z value", z)
j = 10
j %= 4  # ( j = j % 5)
print("j value", j)
