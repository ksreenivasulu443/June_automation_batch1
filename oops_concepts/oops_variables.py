class Calc:
    pi = 3.14  #class variable/static variable

    def __init__(self, a, b):
        self.a = a  # instance variable
        self.b = b  # instance variable
        e=500 #local a=variable
        print("e value is ", e)

    def add(self): # instance method
        print("inside add pi value", self.pi)
        print("inside add e value", self.e)
        c = 100  # local variable
        d = 200  # local variable
        print("hello this is add method")
        return self.a + self.b

    def sub(self):
        return self.a - self.b



obj = Calc(4, 5)
print("id of obj", id(obj))

print("id of obj", id(obj))

print(obj.add())

# obj2 = Calc(4,5)
#
# print("id of obj2", id(obj2))
