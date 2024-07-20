#syntax
import timeit


# while condition:
#     stmts

# while True:
#     print("inside while loop")

num=0
while num<=10:
    print(num)
    if num ==5:
        break
    num = num+1

print("hello this is after while loop")

# num=5
# while num>0:
#     print(num)
#     num = num-1

def sum_with_for_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Function to sum numbers using a while loop
def sum_with_while_loop(n):
    total = 0
    i = 0
    while i < n:
        total += i
        i += 1
    return total

# Measure execution time for the for loop
print("Time taken by for loop:", timeit.timeit(lambda: sum_with_for_loop(1000000000), number=1))

# Measure execution time for the while loop
print("Time taken by while loop:", timeit.timeit(lambda: sum_with_while_loop(1000000000), number=1))
