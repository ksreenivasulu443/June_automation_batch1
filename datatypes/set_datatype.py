"""This module file is create to practice python tuple datatypes
created by Sreeni on 07/03/2024 """

s = { 2.0, True, 1 + 2j, 'etl', False,0,1}


print("set values", s)
print("type of s is ", type(s))
print("memory of s", id(s))

print("methods available in sets", dir(s))
ls = [1,2,2,2,3]
ls = set(ls)
print(list(ls))
s1 ={1,2,3,4}
s2 ={3,4,5}
print("s1.intersection(s2)",s1.intersection(s2))
print("s1.difference(s2)",s1.difference(s2))

s1.add(8)

print("s1 after add", s1)

s1.pop()
print("s1 after pop", s1)

fs = frozenset(s1)

print("fs set values", fs)
print("type of fs is ", type(fs))
print("memory of s", id(fs))
print("methods available in frozen sets", dir(fs))

ji




