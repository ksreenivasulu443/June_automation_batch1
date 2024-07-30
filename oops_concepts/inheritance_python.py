class Parent: # super class
    def __init__(self,name): # parent constructor this method overiden in child class
        print("This is parent constrcutor")
        self.name=name
    def method1(self): # this method is overiden in child class
        print("This is parent class method1")
    @staticmethod
    def method2(): # this method is overiden in child class
        print("This is parent class method2")

class Child(Parent):  #sub class
    def __init__(self): # child constructor #
        super().__init__()
        print("This is child constructor")
    def child_method(self):
        print("this is instance child method")

    def method1(self):
        print("this is child class method1")
    @classmethod
    def method2(cls):
        print("this is child class method2")
        super().method2()

# child = Child()
#
# child.method2()
#
# child.child_method()
#
# child.method1()

# parent = Parent()
#
# parent.method1()


class Child2(Parent):
    pass

child2 = Child2('Sreeni')



