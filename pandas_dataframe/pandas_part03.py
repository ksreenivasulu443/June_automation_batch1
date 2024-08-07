"""This module is created to practice pandas dataframe in python
created by Chandan on 05-08-2024"""

import pandas as pd
import pandasql as ps

df1 = pd.DataFrame({
    'ID':[1,2,3,4],
    'Name':['Alice','Bob','Charlie','David']
})

print("df1 data is:")
print(df1)

df2 = pd.DataFrame({
    'ID':[3,4,5,6],
    'Age':[25,30,35,40]
})

print("df2 data is:")
print(df2)

# merged_df = pd.merge(df1, df2, on='ID', how='inner') #default --> inner join
# print("\ninner merge result:")
# print(merged_df)

print(ps.sqldf("""select * from df1
union
select * from df2"""))

