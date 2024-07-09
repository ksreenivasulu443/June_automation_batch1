student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

m = student.get(2)
m = student.get('marks')
# m = student[2]
m = student['marks']
print(m)

dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)

sampleDict = dict([
    ('first', 1),
    ('second', 2),
    ('third', 3)
])
print(sampleDict)

sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict['class']['student']['marks']['history'])

d1 ={1:'etl', '2':'test'}

print(d1)

sampleDict = {}

print(type(sampleDict))

student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

# del student
#
# student['name']

# del student[0:2]


dict1 = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}
dict2 = dict(dict1)

print(type(dict2))

dict3 = dict1

print(type(dict3))

# dict1 = {"name": "Mike", "salary": 8000}
# temp = dict1.pop("age")
# print(temp)

student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

student.popitem()
print(student)