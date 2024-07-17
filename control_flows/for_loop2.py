# # for loop + range
# # 1. generate 0-5000 numbers sum
# # 2 . prime numbers 0-100 numbers
# # 3. even and odd numbers for 1-400 numbers
# # 4 . squares of sum of 0-100 numbers
#
# r = range(10)
#
# print("type of r", type(r))
#
# print("values of r", r)
#
# # range(stop): Generates numbers from 0 to stop-1.
# # range(start, stop): Generates numbers from start to stop-1.
# # range(start, stop, step): Generates numbers from start to stop-1 with a step of step.
#
# for i in r:
#     print(i)
#
# r2 = range(1, 10)
#
# for i in r2:
#     print(i)
#
# r2 = range(0, 10, 3)
#
# print(r2)
#
# for i in r2:
#     print(i)
#
# # Generate 0-100 numbers sum
#
# r4 = range(0, 101, 1)
# sum1 = 0
# for i in r4:
#     sum1 = sum1 + i
# print(sum1)
#
# factorial of a number 5

# num = int(input("Enter value :"))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
#
# print("factorial",factorial)


# for i in collections:
#     stmts
#     for j in collections:
#         stmts
#         for k in collection:
#             stmts
#             for l in collections:
#                 stmts

# for i in range(1,21):
#     for j in range(1,11):
#         print(f"{i}*{j}=",i*j)
#
# for i in range(1,5):
#     for j in range(10,12):
#         for k in range(20,23):
#             for l in range(30,32):
#                 print(i,j,k,l)

# n=int(input("Enter the number of rows: "))
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()
#
num = 10
for i in range(1,11):
    if i == 5:
        break
    print(f"i value is {i} and {num}/{i}", num/i)

num = 10
while num>0:
    print(num)
    num = num - 1




















