#
# name = 'Sreeni'
# print("name is", name)
#
# name2 = input("enter the name:")
# print("name2 is", name2)
# print("type of name2", type(name2))
#
# age = float(input("enter age value")) # input method converts your input data as string
# print("age is", age)
# print("type age is", type(age))

# if
# if-else
# if-elif
# if-elif-else


# if syntax

# if condition:
# statement
# 4 spaces we call indentation


# name = input("enter name:")
# if name == 'Sreeni':
#     print("hello Sreeni, Good morning")

# if-else
# if condition:
#     #statement
# else:
#     #statement

# name = input("enter name:")
# if name == 'Sreeni':
#     print("Hello Sreeni, Good morning")
# else:
#     print("Hello Guest, Good morning")

# if-elif
# if condition:
#     #statement
# elif condition:
#     #statement
#
# name = input("enter name:")
# if name == 'Sreeni':
#     print("Hello Sreeni, Good morning")
# elif name == 'Rahul':
#     print("Hello Rahul, Good morning")
# elif name == 'Ravi':
#     print("Hello Ravi, Good morning")


# if-elif-else

# if condition:
#     #statement
# elif condition:
#     #statement
# else:
#   #statement

# name = input("enter name:")
# if name == 'Sreeni':
#     print("Hello Sreeni, Good morning")
# elif name == 'Rahul':
#     print("Hello Rahul, Good morning")
# elif name == 'Ravi':
#     print("Hello Ravi, Good morning")
# else:
#     print("hello Guest, Good morning")

# use cases of if-elif-else
# source - csv, json, parquet, txt, .dat, oracle, sqlserver, snowflake, etc
# target - csv, json, parquet, txt, .dat,  oracle, sqlserver, snowflake, etc

# source_type = input("enter your source:").lower()
#
# if source_type == 'csv':
#     print("This is code to read csv files")
# elif source_type == 'json':
#     print("this is code to read json files")
# elif source_type == 'parquet':
#     print("this is code to read parquet files")
# elif source_type == 'oracle':
#     print("this is code to read data from oracle db")
# elif source_type == 'sql_server':
#     print("sql server")
# else:
#     print("enter correct source, currently this code will handle csv, json, praquet, oracle_db")

#user entes number and o/p should be displayed with characters 1-one, 2-two, 3-three

number = int(input("enter number:"))
print("type of number", type(number))

if number == 0:
    print("entered number is Zero")
elif number == 1:
    print("entered number is one")
elif number == 2:
    print("entered number is two")
elif number == 3:
    print("entered number is three")
elif number == 4:
    print("entered number is four")
elif number == 5:
    print("entered number is five")
elif number == 6:
    print("entered number is six")
elif number == 7:
    print("entered number is seven")
elif number == 8:
    print("entered number is eight")
elif number == 9:
    print("entered number is nine")
elif number == 10:
    print("entered number is ten")
else:
    print("entered number is not between 0 and 10, please retry")

# take a number using input method and
# print if num>0 as positive number,
# elif number = 0 print as zero
# else negative number

# take age using input method and
# print if age>=18 as eligible for vote
# else print not eligible and you will be eligible for vote in x years ( x should 18-entered age)


