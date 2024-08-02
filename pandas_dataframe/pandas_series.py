import pandas as pd
import openpyxl

import pandasql as pds
series = pd.Series([1, 2, 3, 4,5], index=['a', 'b', 'c', 'd','e'])
print(series)

print("series['a']", series['a'])
print("series['e']", series['e'])

df = pd.DataFrame(data=series)

print(df.head(3))


data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Creating DataFrame
df_from_dict = pd.DataFrame(data=data_dict)

print(df_from_dict.tail(3))


data_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Creating DataFrame
df_from_list = pd.DataFrame(data=data_list, columns=['Name', 'Age', 'City'])

print(df_from_list.head(2))

df_csv = pd.read_csv(r"/files/sample_csv.csv")

df_excel = pd.read_excel("C:/Users/A4952/PycharmProjects/June_automation_batch1/files/Master_Test_Template.xlsx")

print(df_csv.head(2))

print("df_csv.columns()",df_csv.columns)

print("df_csv.dtypes", df_csv.dtypes)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

print("df_excel.summary", df_excel.describe())

print("selecting phone column data")
print(df_excel['test_case_id'])
print(type(df_excel['test_case_id']))
print("selecting two columns data")
print(df_excel[['validation_Type', 'exclude_columns','execution_ind']])
print(type(df_excel[['validation_Type', 'exclude_columns','execution_ind']]))

# Selecting rows by index
print(df_excel.iloc[0:3, 4:9])  # First row
print(df_excel.iloc[0:2, 0:2])  # First two rows

print(df_excel.loc[0:3,'validation_Type':'schema_path' ])


#print(df_excel[(df_excel.Identifier > 5) & (df_excel.Surname=='Arun')])




# Creating two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Age': [25, 30, 35, 40]
})

# Merging DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Inner join
print("Inner Merge Result:")
print(merged_df)

# Left join
merged_df_left = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Merge Result:")
print(merged_df_left)

# Right join
merged_df_right = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Merge Result:")
print(merged_df_right)

# Outer join
merged_df_outer = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Merge Result:")
print(merged_df_outer)

print("concat axis=0")
concat_df_cols_0 = pd.concat([df1, df2], axis=0)
print(concat_df_cols_0)
print("concat axis=1")
concat_df_cols_1 = pd.concat([df1, df2], axis=0)
print(concat_df_cols_1)




