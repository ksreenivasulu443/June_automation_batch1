# import builtins
#
# # List all built-in functions and exceptions
# print(dir(builtins))
#
# x = "global"
# y = 100


# def outer_function():
#     global a
#     a = 10
#     b = 20
#     c = 30
#     print("global variables inside of function", globals())
#     print("local variables inside of function", locals())
#     print("x value", x)
#     print("y value", y)
#     print("b value ", b)
#
#     def inner_function():
#         d = 137
#         # c=167
#         print("global variables inside of inner function", globals())
#         print("local variables inside of inner function", locals())
#         print("d value", d)
#         print("x,y,a", x, y, a)
#         print("c value", c)
    # inner_function()
    # print("d value",d)


# outer_function()
# print("a value outside of fn",a)
# print("b value ", b)

# z=200
# print("global variables outside of function",globals())
# print("local variables outside of function",locals())


a = 100
b = 20
e= 31
def out_fun():
    a = 24
    c = 21
    print("e value ", e)
    def inner_fun():
        a = 16
        d = 45
        e = 23
        print("e value",e)
        print("global variables outside of function", globals())
        print("local variables outside of function", locals())
    inner_fun()


out_fun()

print("e value",e)













# def outer_function():
#     x = "enclosing"
#     print("globals", globals())
#     print("locals", locals())
#
#     def inner_function():
#         x = "local"
#         print("Inside inner_function:", x)  # Outputs "local"
#
#     inner_function()
#     print("Inside outer_function:", x)  # Outputs "enclosing"
#
#
# outer_function()
# print("In global scope:", x)  # Outputs "global"
