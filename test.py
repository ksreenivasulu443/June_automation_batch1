class Book:
    def __init__(self, pages):
        self.pages = pages


b1 = Book(100)
b2 = Book(200)
# print(b1 + b2)


class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)
print('The Total Number of Pages:',b1+b2)

a=5


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __le__(self,other):
        return self.marks<=other.marks

print("10>20 =",10>20)

s1=Student("Durga",100)
s2=Student("Ravi",200)
print("s1>s2=",s1>s2)
print("s1<s2=",s1<s2)
print("s1<=s2=",s1<=s2)
print("s1>=s2=",s1>=s2)

class Test:
    def m1(self):
        print('no-arg method')
    def m1(self,a):
        print('one-arg method')
    def m1(self,a,b):
        print('two-arg method')

class Test2(Test):
    def m3(self,a,b,c):
        print("3 args")

obj = Test2()

obj.m3(4,5)


