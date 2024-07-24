

# class name0ftheclass:
#     def __init__(self):
#         stmts
#
#     def method1(self):
#         stmts

class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("hello this is constructor")

    def add(self):
        print("hello this is add method")
        return self.a+self.b
    def sub(self):
        return self.a-self.b

obj = Calc(4,5)

obj.__init__(5,11)

#obj2 = Calc(7,8)

#obj.add()

#print(obj.add())
#
# obj2 = Calc(7,9)
#
# print(obj2.sub())

def add(a,b):
    return a+b

add(4,5)


class College:
    def __init__(self):
        pass
    def __init__(self,a):
        self.a=a
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def student(self):
        print("this is student method")

obj3 = College()

#obj3.student()
