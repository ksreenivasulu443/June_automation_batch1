def greeting():  # parameters are optional
    print("Hello Guest, Good morning")


# greeting()

def greeting(name):
    if name == 'Rahul':
        print("Hello Rahul, Good morning")
    else:
        print("Hello Guest, Good morning")


# greeting(name='Sreeni')


#
# greeting(name='Rahul')

def greeting(name, time):
    if name == 'Rahul' and time <= 12:
        print("Hello Rahul,Good morning")
    elif name == 'Rahul' and 12 < time <= 16:
        print("Hello Rahul,Good afternoon")
    elif name == 'Rahul' and time > 16 and time <= 20:
        print("Hello Rahul,Good evening")
    else:
        print("hello guest")


# greeting('Rahul',23)


def calc(a, b):
    print("value of a ", a)
    print("value of b ", b)
    print("sum of a & b is ", a + b)


# calc(5,6) # 5,6 are positional arguments
# calc(a=10, b=20) # a=10 & b=20 are keyword arguments
# calc(b=20,a=5)
# calc(10, b=20)  # 10 is positional argument and b=20 is keyword argument
#
# calc(a=10, 20) # a is keyword arg and 20 is positional args,
#                 # we always need to provide keyword args after positional argument
# calc(10, a=20) # calc() got multiple values for argument 'a'
# calc(b=20,10)

#calc(a=5, b=10)

def calc(a, b, c=0, d=-1): # c, d are default paremeters
    print("value of a ", a)
    print("value of b ", b)
    print("value of c",c)
    print("value of d ", d)
    print("sum of a, b,c,d is ", a + b+c+d)

calc(10,20)# c & d will taken from function definition
calc(10,20,100,200) # c & d values will be taken from fn call
calc(10,20,d=200)



