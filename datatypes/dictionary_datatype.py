"""This module file is create to practice python dictionary datatypes
created by Sreeni on 07/04/2024 """
import pandas as pd

s = set()
d = {}
d1 = {1}

print("type of d", type(d))
print("type of s", type(s))
print("type of d1", type(d1))

# syntax variable_name = {key1:value1,key2:value2, key3:value3}
d2 = {1: 'sreeni', 2: 'Raghav', 3: 'Hari'}
print("type of d2", type(d2))
print("values in d2", d2)

print("Methods available in dict", dir(d2))

# adding and update

d2[4] = 'Janav'
print("d2 after adding key4", d2)
d2[1] = 'Sreenivas'
print("d2 after update key1 value to Sreenivas", d2)

d2.update({5:'Somu', 6:'babu', 2:'Raghavendra',7:'Hari'})
print("d2 after update method", d2)

print("keys in d2", d2.keys())
print("type of d2.keys()", type(d2.keys()))
print("values in d2", d2.values())
print("type of d2.values()", type(d2.values()))
print("items in d2", d2.items())
print("type of d2.items()", type(d2.items()))
# d2.pop(7)
# print("after pop d2", d2)
# d2.pop(6)
# print("after second time pop d2", d2)
#
# d2.popitem()
# print("after popitem d2", d2)
#
# d2.popitem()
# print("after popitem d2", d2)

# to access elements

print(d2)
print("d[4]",d2[4])

print("get method", d2.get(4))

print(d2)
d2.pop(1)
print(d2)

print(help(d2.pop))

print(pd.DataFrame(d2))








# d3 = {1:['sreeni', 'M','ETL'], 2:['Raghav','M','JAVA',"17-06-2009"]}
#
# print(d3)

