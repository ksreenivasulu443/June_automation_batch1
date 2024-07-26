a = 5
b= 10

print(a.__add__(b))

4+5

# print("methods available on a", dir(a))

class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages
    def __sub__(self, other):
        return 56575

    def __mul__(self, other):
        return self.pages*other.pages



b1 = Book(100)
b2 = Book(200)
print("number of pages in b1 and b2", b1+b2)
print("sub b1 and b2", b1-b2)
print("mul b1 and b2", b1*b2)


class Test:

    def m1(self,*args):
        print('two-arg method')
obj = Test()

obj.m1()

class Test:
    def __init__(self):
        print('no-arg method')
    def __init__(self,a):
        print('one-arg method')
    def __init__(self,*args):
        print('two-arg const method')



obj = Test(2,3,4)

