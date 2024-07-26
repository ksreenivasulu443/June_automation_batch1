#constructor over loading

class Student:

    def __init__(self):
        print("no arg")

    def __init__(self,a):
        print("one arg")

    def __init__(self,a,b):
        print("two arg")

    def __init__(self,*args):
        print("multi arg")

obj = Student(11,22,33) #latest constructor will be executed