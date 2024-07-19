
# def greeting():
#     print("hello guys ,Good mornimg")
#
# #greeting()
#
# def greeting(name):
#     if name =='Rahul':
#         print("hello Rahul ,Good mornimg")
#     else:
#         print("hello Guest ,Good mornimg")

#greeting('suketh')


def greeting(name,time):
    if name =='Rahul' and time<12:
        print("hello Rahul ,Good mornimg")
    elif(name =='Rahul' and time>12 and time < 16):
        print("hello Rahul ,Good afternoon")
    elif (name == 'Rahul' and time > 16 and time < 19):
        print("hello Guest ,Good evening")
    else:
        print("Hello guest")

#greeting('Rahul',13)



def cal(a, b):
    print(f" Value of a", a)
    print(f" Value of b",b)
    print(f" Add value of two numbers", a + b)

cal(10,20) # positioanl arguements
cal(a=30 , b=20) #keyword arguments
cal(10,b=20) #10 is positional; and b=20 is keyword usage
# cal(a=10,10) #  key word arguement is a=10 and 10 positioanl
# #always remeber we should not provide  positional arguements after keyword arguements



def  is_even_odd(num):
    if num%2 == 0:
        print("even")
    else:
        print("odd")
    return num,10,20

print(is_even_odd(10))
