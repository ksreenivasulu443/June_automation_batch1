# #string, list, tuple, dict, set, frozenset
#
# str1 = 'ETL Automation'
#
# print("'E' in str1", 'E' in str1)
#
# print("'S' in str1", 'S' in str1)
#
# print("'E' not in str1", 'E' not in str1)
#
# print("'S' not in str1", 'S' not in str1)
#
# ls1 = [1,2,3,4]
#
# print("1 in ls1", 1 in ls1)
# print("5 in ls1", 5 in ls1)
#
# print("'3' in ls1", "3" in ls1)

ls1 = [1,2,3]
ls2 = [1,2,3,[1,2,3]]

print("ls1==ls2",ls1 == ls2)
print("ls1 in ls2", ls1 is ls2)
d1 = {1:'ETL', 2:'Automation', 3:'testing'}
print("1 in d1", 1 in d1) # syntax search for only keys
print("d1.values",d1.values())
print("Automation in d",'Automation' in d1.values()) # search for values
print("5 in d",5 in d1.keys())

d1 = {1:'ETL', 2:'Automation', 3:'testing'}
d2 = {1:'ETL', 2:'Automation', 4:'testing'}


print('id of d1', id(d1))
print("id of d2 ", id(d2))
print("d1 is d2", d1 is d2)

print("d1==d2", d1==d2)



