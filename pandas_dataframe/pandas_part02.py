import pandas as pd
import pandasql as ps
import openpyxl

#read excel
df = pd.read_csv(r"C:\Users\ichan\PycharmProjects\June_automation_batch5\files\Contact_info.csv")
print(df.head(3))

#iloc --> this means identifier location, we can use it for slicing
print("df.iloc[0:3]")
print(df.iloc[0:3]) #3 rows --> 0 to n-1 --> 0 to 2
print(df.iloc[0:3, 1:2]) #row & column filter --> 0 to 2 rows, inside this 1 column will be printed

#loc --> location function
print(df.loc[0:2, 'Surname':'given_name']) #there is no n-1, 0 to 2 rows selected, in this surname to give_name printed


#filter data --> i want identifier greater than 1 #or & and condition we can use
print("df[df.Identifier > 5]:")
print(df[df.Identifier > 5])

print("df[(df.Identifier > 5) & (df.Surname == 'Arun')]")
print(df[(df.Identifier > 5) & (df.Surname == 'Arun')])


