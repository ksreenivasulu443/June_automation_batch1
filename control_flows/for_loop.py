#
# ls = [1,2,3,4,5]
# ls_squares = []
#
# for i in ls:
#     print("i value is:", i)
#     ls_squares.append(i*i)
#
#
# print(ls_squares)
#
# t = (1,2,3,4,5)
# t_squares=[]
#
# for i in t:
#     print("i value is:", i)
#     t_squares.append(i*i)
#
# print(t_squares)

# mul=1
# t = [1,2,3,4,5]
# for i in t:
#     mul = mul*i
#
# print("mul ", mul)
#
# sum =0
# for i in t:
#     sum = sum+i
# print("sum", sum)
#
ls = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,19,100]

even_sum = 0
odd_sum = 0

for i in ls:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
#
# print("total sum", even_sum+odd_sum)
# print("even sum", even_sum)
# print("odd sum", odd_sum)
#vowels a,e,i,o,u
# str1 = 'sky'
# flag = 0
# for i in str1.lower():
#     if i in ['a','e','i','o','u']:
#         print("vowel present")
#         break
#     else:
#         print("vowel not present")
#         break

str1 = 'ETL Automation'  #sKY
str2=''
for i in str1:
    if i.islower():
        str2 = str2+i.upper()
    elif i.isupper():
        str2 = str2+i.lower()

print("Str2", str2)























