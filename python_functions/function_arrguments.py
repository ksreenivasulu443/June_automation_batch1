"""This module is created to practice function arrguments in python
created by Chandan on 22-07-2024"""

def f(arg1,arg2,arg3=4,arg4=8): #arg3 & arg4 are default arguments
    print(arg1,arg2,arg3,arg4)
f(3,2) #all are positional arguments #Result --> 3,2,4,8
f(10,20,30,40) #all are positional arguments #Result --> 10,20,30,40
f(25,50,arg4=100) #25,50 Positional arguments, 4 is default & 100 is keyword argument #Result --> 25,50,4,100
f(arg4=2,arg1=3,arg2=4) #Result --> 3,4,4,2 #2,3,4 keyword arg, arg3=4 is default
#f() #result is error #missing two positional arguments
#f(arg3=10,arg4=20,30,40) #error #positional arg should come first
#f(4,5,arg2=6) #error #multiple values for arg2
#f(4,5,arg3=5,arg5=6) #error #there is no arg5
#f(4,5,5,arg3=2) #error #multiple values for arg3