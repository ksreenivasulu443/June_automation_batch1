# project
#     packages1
#         modules1
#             functions1,2,3
#     package2
#         module2
#             functions 4,5,6



def calc(a,b, type):
    if type == 'add':
        print(f"sum of a & b is", a+b)
    elif type == 'sub':
        print(f"sub of a & b ", a-b)
    elif type == 'mul':
        print(f"multiplication of two numbers", a*b)
    elif type == 'div':
        print(f"division of two numbers", a/b)
    else:
        print("incorrect type calcualation")







