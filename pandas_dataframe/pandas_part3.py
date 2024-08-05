import pandas as pd
import pandasql as ps
# Creating two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4,1],
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Alice']
})
print("df1 data is:")
print(df1)

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Age': [25, 30, 35, 40]
})

print("df2 data is:")
print(df2)

#help(pd.merge)

# Merging DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Inner join
print("Inner Merge Result:")
print(merged_df)

#Left join
merged_df_left = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Merge Result:")
print(merged_df_left)
#
# Right join
merged_df_right = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Merge Result:")
print(merged_df_right)
#
# Outer join
merged_df_outer = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Merge Result:")
print(merged_df_outer)

print(ps.sqldf("""select df1.id,df1.name, df2.age from df1 inner join df2 on df1.id=df2.id"""))

print(ps.sqldf("""select df1.id,df1.name, df2.age from df1 full outer join df2 on df1.id=df2.id"""))
print(ps.sqldf("""select id, count(1) from df1 group by id"""))
print(ps.sqldf("""select min(id), max(id), avg(id), count(1) from df1"""))

#union all( rules, number columns, type of columns and orader should be same)
print("concat axis=0")
concat_df_cols_0 = pd.concat([df1, df2], axis=0)
print(concat_df_cols_0)
print("concat axis=1")
concat_df_cols_1 = pd.concat([df1, df2], axis=0)
print(concat_df_cols_1)
#
# from ydata_profiling import ProfileReport
#
# Result = ProfileReport(df1)
#
# Result.to_file("profile_report.html")

df3 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'fname': ['Alice', 'Bob', 'Charlie', 'David']
})
print("df1 data is:")
print(df3)

help(pd.concat)

print(pd.concat([df1, df2,df3], axis=1))

print(ps.sqldf("""select * from df1
                union
                select * from df2
                union 
                select * from df3"""))
