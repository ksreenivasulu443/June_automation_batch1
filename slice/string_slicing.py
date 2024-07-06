"""This module file is create to practice python string slicing
created by Sreeni on 06/28/2024
"""




 # Python index starts from 0
 # python index end value is len(str)-1
 # to slice any iterative data(str, list, tuple, df, array, etc) using python we have to use square brackets []

 # syntax to slice iterative data : str[start pos : end pos : step],
# start pos is mandatory, end pos - optional, step - optional, default step value is +1

str = 'ETL AUTOMATION'
print("str value is ", str)

print("Zero position character", str[0])
print("first position character", str[1])
print("9th position character", str[9])
print("13th position character", str[13])



print("slice string from 0 to 2 position",str[0:3])

print("Slice automation from ETL AUTOMATION string",str[20:25])

print("str[3:7]", str[3:7], len(str[3:7]))

print("str[4:14:2]", str[4:14:2])
print("str[4:14:3]", str[4:14:3])

print("-1st position character", str[-1])
print("-2nd position character", str[-2])
print("-3rd position character", str[-3])
print("-14th position character", str[-14])
print("-15th position character", str[-16])







