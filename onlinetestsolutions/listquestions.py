my_list = ["Hello", "Python"]
print("-".join(my_list))

list1 = ['xyz', 'zara', 'pYnative']
print(min(list1))

# list1 = [1,2,3,3,'1']
# print(min(list1))

sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1:1])

aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])

listOne = ['a', 'b', 'c', 'd']
listTwo = ['e', 'f', 'g']

# newList = listOne + listTwo
#
# print(newList)

# newList = extend(listOne, listTwo)


a= listOne.extend(listTwo)

print(a)

# newList.extend(listOne, listTwo)

sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

aList = [4, 8, 12, 16,2,7]
aList[1:3] = [20, 24]
print(aList)

aList = [5, 10, 15, 25]
print(aList[::-1])

sampleList = [10, 20, 30, 40]
del sampleList[6:]
print(sampleList)

l = [None] * 10
print(len(l))

print(l)
