import pandas as pd

data_dict = {'Name':['Alice','Bob','Charlie'],
             'Age':[25,30,35],
             'City':['New York','Los Angeles','Chicago']}

#creating data frame
df_from_dict = pd.DataFrame(data_dict)
print(df_from_dict) #all rows
print()
print(df_from_dict.head(3)) #top two rows
print()
print(df_from_dict.tail(2)) #last two rows