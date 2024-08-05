import pandas as pd
import pandasql as ps
import openpyxl

import pyarrow
#import fastparquet



help(pd.read_csv)

df = pd.read_csv(filepath_or_buffer='C:/Users/A4952/PycharmProjects/June_automation_batch1/files/Contact_info.csv')
# df2 = pd.read_csv(filepath_or_buffer = "C:\\Users\\A4952\\PycharmProjects\\June_automation_batch1\\files\\Contact_info.csv")
# df3 = pd.read_csv(filepath_or_buffer = r"C:\Users\A4952\PycharmProjects\June_automation_batch1\files\Contact_info.csv")

print("type of df", type(df))

# C:\Users\A4952\PycharmProjects\June_automation_batch1\files\Contact_info.csv
print(df.head(3))  # top n records
print(df.tail(3)) # bottom n record

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

print(df.head(3))  # top n records
print(df.tail(5)) # bottom n record

print("number of rows and columns", df.shape[0], df.shape[1])

print("shape of df", df.shape)

print("all columns in df", df.columns)
print(" datatypes of each column", df.dtypes)

print("summary of dataframe data:")
print(df.describe())

print("select one column from dataframe")
print(df['zipcode'])

print("select one column from dataframe using pandasql")
duplicate = ps.sqldf("""select identifier, count(1) as cnt from df group by identifier 
                having count(1)>1""")

df2 = pd.read_excel(r"C:\Users\A4952\PycharmProjects\June_automation_batch1\files\Master_Test_Template.xlsx")
print(df2.head(3))

print("df.iloc[0:3]:")
print(df.iloc[0:9, 0:18])  # First row
print("df.loc[0:3]:")
print(df.loc[0:2, 'Surname':'given_name' ])  # First two rows
print("df[(df.Identifier > 5) & (df.Surname == 'Arun')  ]:")
print(df[(df.Identifier > 5) &  (df.Surname == 'Arun') ])

df3 = pd.read_parquet(r"C:\Users\A4952\PycharmProjects\June_automation_batch1\files\userdata1.parquet")
print(df3)




