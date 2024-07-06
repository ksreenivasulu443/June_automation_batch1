"""This module file is create to practice python tuple datatypes
created by Sreeni on 07/03/2024 """

t = (1, 2.0, True, 1 + 2j, 'etl')



print("tuple values", t)
print("type of t is ", type(t))
print("memory of t", id(t))

print("first element in t is ", t[0], type(t[0]), id(t[0]))
print("second element in t is ", t[1], type(t[1]), id(t[1]))
print("third element in t is ", t[2], type(t[2]), id(t[2]))
print("fourth element in t is ", t[3], type(t[3]), id(t[3]))
print("fifth element in t is ", t[4], type(t[4]), id(t[4]))
print("t[1:3] ", t[0:3], type(t[0:3]), id(t[0:3]))
print("methods available in tuple type", dir(t))


t2 =(1,2,2,2,2,4,4,4,4,4,4,4,4,4,6,2,2)

print("count of 4", t2.count(4))

print("index of 4", t2.index(4))

t = ('localhost','user','password')

lat_long = (17.54545, 76.5362532)


t[0] = 'localhost2'

print(t)





