"""This file created to practise python string methods
and created by Sreeni on 25/Jun/2024"""
import pandas as pd
# str7 = 'ETL Automation testing'
# print("Before capitalize str7 is ", str7)
# print("After capitalize str7 is", str7.capitalize())
# print("After title str7 is", str7.title())
# print("After lower str7 is", str7.lower())
# print("After upper str7 is", str7.upper())
# print("After casefold str7 is", str7.casefold())
# print("Before swapcase str7 is ", str7)
# print("After swapcase str7 is", str7.swapcase())
#
# txt = "ETL Testing validation has started"
# x = txt.center(80, '-')
# print(x)
#
# str8 = 'BIG DATA TESTING | ETL Testing | AUTOMATION testing'
# print(f"count of A in {str8}", str8.count('E'))
#
#
# print(f"count of | in {str8}", str8.count('|', 20,25))
#
# str1 ='ETL TEST'
#
# print("count of E", str1.count('E',1,6))
#
#
# table1='emp3'
# table2 = 'dept3'
# col='deptno3'
# query =  f""" select * from {table1} a, {table2} b
#          where a.{col}=b.{col} """
#
# print(query)
#
# str9 ='ETLTESTING1234e'
#
# print("endswith 'ING'", str9.endswith('Testing'))
# print("startswith 'ETL'", str9.startswith('ETL'))
#
# print("isalpha", str9.isalpha())
# print("isalphanum", str9.isalnum())
#
# print("isupper", str9.isupper())
#
# txt = "565543e"
#
# x = txt.isnumeric()
#
# print("txt is numeric", x)
#
# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for &sup2;
# c = "10km2"
# d = "-1"
# e = "1.5"
#
# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())
#
# text ='Sreeni'
#
# text.isnumeric()
#
# print(dir(10))
#
#
# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"
#
# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())
#
# myTuple = ["John", "Peter", "Vicky"]
#
#
# x = ",".join('sreeni','K')
#
# print(x)

columns = 'col1-col2-col3'


# null_values = col1,col2,col3

# print("type of columns, split output, split output type",type(columns), columns.split("-"), type(columns.split(",")))

df = pd.read_csv("/Users/harish/PycharmProjects/june_batch/Contact_info.csv")
print("df columns",df.columns)
columns = df.columns
key_cols = ",".join(columns)

print(key_cols)

sql = f"select {key_cols} from tablename"

print(sql)






