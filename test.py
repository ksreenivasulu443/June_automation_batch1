import numpy as np

from pandasql import sqldf

array1 = np.array([[1,2,3,5],[5,6,7,7],[7,8,9,10]])

array2 = np.array([1,'a','c'])

print(array1)

print(type(array2))

print(type(array2[1]))
print(type(array2[2]))



import pandas as pd

df = pd.DataFrame(data=array1, columns=['col1','col2','col3','col4'])

print(df.head())

import pandas as pd

# Dictionary with lists as values
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Creating DataFrame
df_from_dict = pd.DataFrame(data_dict)

print(df_from_dict)

print("sqldf")
print(sqldf("select name from df_from_dict"))


import pandas as pd

# List of lists
data_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Creating DataFrame
df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])

print(df_from_list)




