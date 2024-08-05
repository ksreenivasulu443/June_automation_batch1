class Calc:
    def __init__(sreeni,a,b):
        sreeni.a=a
        sreeni.b=b
        print("memory of self", id(sreeni))

    def add(sreeni):
        print("hello this is add method")
        return sreeni.a+sreeni.b

obj = Calc(4,5)

print("memory of obj", id(obj))

print(obj.__dict__)

print(obj.add())