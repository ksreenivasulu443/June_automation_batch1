class Calc:
    pi = 3.14  #class variable
    a=100

    def __init__(self, a, b):
        self.a = a  # instance variable
        self.b = b  # instance variable
        print("id of self", id(self))
    def add(self): # instance method
        self.c=360
        return self.a + self.b

    def sub(self): # instance method
        return self.a - self.b
    @classmethod
    def aread_of_circle(cls,r): # class method
        print("id of cls", id(cls))
        print("a value", cls.a)
        return cls.pi*r*r
    @staticmethod
    def area_square(l,b): # static method
        return l*b




obj = Calc(4, 5)
print("id of obj", id(obj))

print(obj.__dict__)

print(obj.add())

print(obj.__dict__)

obj.d=560

print(obj.__dict__)

print(obj.a)

# print(obj.aread_of_circle(3))
#
# print(obj.area_square(4,5))




# class read_data:
#     read_nosqldb = 'nosql db config' - 1kb
#
#     def __init__(self, type_of_file, type_of_db):
#         self.type_of_file = type_of_file  # instance variable 1gb
#         self.type_of_db = type_of_db  # instance variable 1gb
#
#     def read_file(self):
#        return 'file_data'
#
#     def read_db(self):
#        return 'db_data'
#
#     @classmethod
#     def read_nosqldb(cls):
#         return 'nosqldb data'
#
