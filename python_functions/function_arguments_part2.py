# def calc(a, b):
#     print("sum of a & b is ", a + b)
#
# calc(3,4)
# def calc(a, b,c):
#     print("sum of a, b,c is ", a + b+c)
#
# calc(3,4,5)
#
# #calc(3,4,5,6)
# calc(2,3)

def calc(*args):
    # print(args)
    # print("args typs", type(args))
    sum_1 = 0
    for i in args:
        sum_1 = sum_1 + i
    print(f"sum of {args} is", sum_1)
    return sum_1


# calc(3,4)
# sum_out = calc(5, 6, 7, 7, 8, 8)  # positional variable length arguments
# print("sum_out", sum_out)
# calc(5, 6, 7, 7, 8, 8, 374632, 65743275, 7462534, 7635642)
# calc(5)


def calc(**kwargs):
    print(kwargs)
    print("args typs", type(kwargs))
    sum_1 = 0
    for i in kwargs.values():
        sum_1 = sum_1 + i
    print(f"sum of {kwargs}", sum_1)


#calc(a=10, b=20, c=30, d=40, e=10, f=50)


def greeting(**kwargs):
    print(kwargs)
    print_message = ''
    for i in kwargs.values():
        print_message = print_message + " " + i
    print(print_message)


#greeting(name='Sreeni', message="how are you", message2='Good morning')


def f(arg1, arg2, arg3=4, arg4=8): # arg3,4 default arguments
    print(arg1, arg2, arg3, arg4)

#f(3,2)# 3,2 positional arguments
#f(10,20,30,40) # 10,20,30,40 positional arguments
#f(25,50,arg4=100) # 25,50 positional arguments, 4 - default arg, 100 -keyword argument
#f(arg4=2,arg1=3,arg2=4) # 2,3,4 keyword word args, arg3=4 is default arg
#f()
#f(arg3=10,arg4=20,30,40)
#f(4,5,arg2=6)
#f(4,5,arg3=5,arg5=6)
#f(4,5,5,arg3=2)

# def display_person(*args):
#     for i in args:
#         print(i)
#
# display_person(name="Emma", age="25")

def fun1(num):
    print(num)


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)


def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)








