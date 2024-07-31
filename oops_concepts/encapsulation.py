class MyClass:
    def __init__(self, a):
        self.a = a  # Public attribute
        print("value of a from cons",a)

    def public_method(self):
        print("value of a from public method", self.a ) # Public method

# obj = MyClass(10)
# obj.public_method()
#
# print("a value from outside of class", obj.a)



class MyClass:
    def __init__(self, a):
        self._a = a  # Protected attribute
        print("value of a from cons", self._a)

    def _protected_method(self): # Protected method
        print("value of a from public method", self._a)

# obj = MyClass(20)
# obj._protected_method()
#
# print("a value from outside of class", obj._a)

class MyClass:
    def __init__(self, a,b):
        self.__a = a  # Private attribute
        self.b=b
        print("value of a from cons", self.__a)

    def __private_method(self):
        print("value of a from public method", self.__a)

    def get_value(self):
        print("value of a from get value method", self.__a)


obj = MyClass(30,40)
obj.get_value()

print("b value from outside of class", obj.b)
print(obj.__a)



