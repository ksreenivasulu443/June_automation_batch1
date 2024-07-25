#self is the current object memory
#self.a, self.b -- we are passing these values to object memory

class Calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("memory of self is:", id(self))

    def add(self):
        return self.a + self.b


obj = Calc(4,5)
print("memory of object:",id(obj))

#here self & object have same memory
#values are added to self memory, we use self to store values or retreive values
print(obj.__dict__) #this will show the parameters & values assigned
obj.add()


