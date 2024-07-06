"""This module file is create to practice python list datatypes
created by Sreeni on 07/02/2024 """

ls = [1, 2.0, True, 1+2j, 'string', (1,2),[1,2]]

print("list values", ls)
print("type of ls is ", type(ls))
print("memory of ls", id(ls))

print("first element in ls is ", ls[0], type(ls[0]),id(ls[0]))
print("second element in ls is ", ls[1],type(ls[1]),id(ls[1]))
print("third element in ls is ", ls[2],type(ls[2]),id(ls[2]))
print("fourth element in ls is ", ls[3],type(ls[3]),id(ls[3]))
print("fifth element in ls is ", ls[4],type(ls[4]),id(ls[4]))
print("sixth element in ls is ", ls[5],type(ls[5]),id(ls[5]))
print("last element in ls is ", ls[6],type(ls[6]),id(ls[6]))

print("ls[0:4]", ls[0:4:1])

ls2 = []
#ls2 = list()
print("list2 values", ls2)
print("type of ls2 is ", type(ls2))
print("memory of ls2", id(ls2))

print("methods available in list", dir(ls2))

print("after append")
ls2.append(5) # append will add element at end of list
print("list2 values", ls2)
print("type of ls2 is ", type(ls2))
print("memory of ls2", id(ls2))
ls2.insert(0,4)
print("after insert")
print("list2 values", ls2)
print("type of ls2 is ", type(ls2))
print("memory of ls2", id(ls2))

ls2.extend((1,2,3,4,4,4,4,6,5,4,4,6,1))
print("list2 values", ls2)

print("count of 4 ", ls2.count(4))

ls3 = ls2.copy()
print("ls3", ls3)
print("ls2", ls2)

ls2.pop(5)
print("after pop")
print("ls2", ls2)
print("ls3", ls3)

print("ls4 is pointed to ls2")
ls4 = ls2

print("ls2", ls2)
print("ls4", ls4)

ls2.remove(1)
print("after remove")
print("ls2", ls2)
print("ls4", ls4)

ls2.append('sreeni')
print("after append")
print("ls2", ls2)
print("ls4", ls4)

ls5 = [3,'sreeni', 10.3,1,2]
print("ls5", ls5)
print("ls5[1][::-1]", ls5[1][::-1])
ls5.reverse()
print("after reverse")
print("ls5", ls5)
#
# print("ls5[3][::-1]", ls5[3][::-1])
#
# ls6 = [1,1,2,2,2,2,2,5,'sreeni']
# print("ls6", ls6)
# #ls6.remove(2)
#
# ls6 = list(set(ls6))
# ls6.remove('sreeni')
# print(ls6)
# print("ls6 after remove", ls6)
#
#
#
#
# ls8 = [1.3, 2.5, 'Ajay', 'ravi']
#
# ls8.pop(2)
#
# # ls9 = ls8.remove('Ajay')
# # print('ls9', ls9)
#
# ls9 = ls8.copy()
#
# ls = [1,2,3]
# ls2 = [3,4,5]
# print("list addition ls, ls2", ls+ls2)
# print("list mul ls", ls*2)
#
# # + --> contact two string  and add two values
# # * --> repeat values and multiply two number
#
# fname ='Sreeni'
# lname ='kattu'
# a=10
# b=20
# print("fname+lname", fname+lname)
# print("a+b", a+b)
# print("a*b", a*b)
# print("fname*2", fname*2)
#
# t = (1,2,3)
# ls=[1,2,3]
# print("before convert",type(ls))
# print("before convert",type(t))
# ls = tuple(ls)
# print("after convert to tuple",type(ls))
# t = list(t)
# print("after convert to list",type(t))
#
#
#
#
