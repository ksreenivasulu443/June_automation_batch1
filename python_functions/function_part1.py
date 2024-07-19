def cal(a, b):
    print(f" Value of a", a)
    print(f" Value of b",b)
    print(f" Add value of two numbers", a + b)
    print(f" Sub value of two numbers", a - b)
    print(f" Mul value of two numbers", a * b)
    print(f" Div value of two numbers", a / b)
    return a+b , a-b ,a*b ,a/b

sum,sub,mul,div = cal(20,10)

print(f"sum,sub,mul,div",sum,sub,mul,div)
print(f"sub",sub)
# a=float(input("enter the a value:"))
# b=float(input("enter the b value:"))
# cal(a,b)
# cal(10, 8) #fumction call to call to specific functions
#cal(11, 22) #fumction call to call to specific functions

# def count_check(source_count,target_count):
#     if(source_count == target_count):
#         print(f"count is matching")
#     else:
#         print(f"count is not matching and difference is", source_count-target_count)
#
#
# count_check(10,10)
