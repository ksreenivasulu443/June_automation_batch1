"""This module file is create to practice python list datatypes
created by Sreeni on 07/02/2024 """

ls = [1, 2.0, True, 1 + 2j, 'etl', [1, 2],
      (1, 2)]  # We are able to store different datatypes data this nature we call it as heterogeneous data storage

print("list values", ls)
print("type of ls is ", type(ls))
print("memory of ls", id(ls))

print("first element in ls is ", ls[0], type(ls[0]), id(ls[0]))
print("second element in ls is ", ls[1], type(ls[1]), id(ls[1]))
print("third element in ls is ", ls[2], type(ls[2]), id(ls[2]))
print("fourth element in ls is ", ls[3], type(ls[3]), id(ls[3]))
print("fifth element in ls is ", ls[4], type(ls[4]), id(ls[4]))
print("sixth element in ls is ", ls[5], type(ls[5]), id(ls[5]))
print("last element in ls is ", ls[6], type(ls[6]), id(ls[6]))

ls = [1, 2, 3, 4, 5]

print("list values", ls)
print("type of ls is ", type(ls))
print("memory of ls", id(ls))

print("methods available in list", dir(ls))

ls2 = list()  # empty list
ls3 = []  # empty list
print("list values", ls2)
print("type of ls is ", type(ls2))
print("memory of ls", id(ls2))

# append,insert, extend
print("ls2 before append", ls2)
ls2.append(24.5)
print("ls2 after append", ls2)
ls2.append('etl')
print("ls2 after append etl", ls2)
ls2.append(8)
print("ls2 after append etl", ls2)
ls2.append(True)
print("ls2 after append etl", ls2)
ls2.append([1, 2])
print("ls2 after append etl", ls2)

# extend
ls2.extend([4, 5, 6, 4, 5, 6])
print("ls2 after extend ", ls2)

ls2.extend('ETL')  # extend method takes iterable data as i/p, we can pass list, tuple, dict,set,fs, string
print("ls2 after extend ", ls2)
ls2.extend([4, 5, 6])
print("ls2 after extend ", ls2)

ls2.insert(3,'AUTOMATION')

print("ls2 after insert ", ls2)

ls2[1]='ETL'
print("ls2 after update ", ls2)

#clear, pop, remove
print("ls2 before pop", ls2)
ls2.pop(-2) # pop will be used to remove element from specified index value, if index is not passed last element will be removed
print("ls2 after pop",ls2)

ls2.remove(4) # remove will take value that we wanted to remove
print("ls2 after remove",ls2)
ls2.remove(4) # remove will take value that we wanted to remove
ls2.remove(4)
print("ls2 after remove",ls2)

ls2.clear()

print("ls2 after clear",ls2)

ls2 = [1,2,2,3,4,44,5,5,5,5,5,5,5,6,7,7]

print("count of 7", ls2.count(1))

ls2.reverse()

print("ls2 after reverse", ls2)

ls2.sort(reverse=True)
print("ls2 after sort", ls2)

unique_element_in_ls2 = set(ls2)

print(unique_element_in_ls2)
ls = [1, 2, 3, 4, 5,8]
print(len(ls))

ls =[1,2,3]
ls2 =[4,5,6]
print(ls*3)

