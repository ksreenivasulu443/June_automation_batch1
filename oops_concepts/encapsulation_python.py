class MyClass:

    def __init__(self,a):
        self.__a = a #protected attribute
        print("value of a is:",self.__a)

    def __private_method(self): #protected method
        print("value of a from private method is:", self.__a)

    def get_value(self): #public method
        print("Value of a from get_value is:",self.__a)

obj = MyClass(10) #constructor is executed #Result -->10
#obj.__private_method() #we can't access outside of class
#obj.__a #we can't access outside of class
obj.get_value() #this we can access anywhere

