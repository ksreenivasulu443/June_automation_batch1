

def calculation(a,b): # function definition
    print("value of a is", a)
    print("value of b is", b)
    print("sum of a & b is ", a+b)
    #return a+b

# a= float(input("enter a value: "))
# b= float(input("enter b value: "))
# cal(a,b)  # function call to call specific function

def count_check(source_count, target_count):
    if source_count == target_count:
        print("count is matching")
    else:
        print("count is not matching and difference is ", source_count-target_count)

def calculation(a,b): # function definition
    # print("value of a is", a)
    # print("value of b is", b)
    # print("sum of a & b is ", a+b)
    return a+b, a-b


def calculation(a,b): # function definition
    # print("value of a is", a)
    # print("value of b is", b)
    # print("sum of a & b is ", a+b)
    return a+b, a-b, a*b, a/b

# sum, sub,mul,div = calculation(4,6)
#
# print("sum,sub", sum,sub)
# # print("sub", sub)
# # print("mul", mul)

print(calculation(a=4,b=5))

