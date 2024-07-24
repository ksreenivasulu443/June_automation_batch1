class calc():
    def __init__(self, a,b):
        self.a=a
        self.b=b
        print("this is __init__")
        print(id(self))

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

obj = calc(a=1,b=2)

#obj2 =  calc(4,5)

print(obj.a)
print(id(obj))
print(obj.b)
print(obj.add())

class scientificcal(calc):
    def __init__(self,a,b):
        self.a=a
        self.b =b

obj = scientificcal(4,5)

print("add poly", obj.add())

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# Access to the balance is controlled through methods
account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # Output: 150
