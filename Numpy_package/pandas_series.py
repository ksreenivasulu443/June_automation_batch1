import pandas as pd
series = pd.Series([1, 2, 3, 4,5], index=['a', 'b', 'c', 'd','e'])
print(series)

print("series['a']", series['a'])
print("series['e']", series['e'])

df = pd.DataFrame(series)

print(df.head(3))


data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Creating DataFrame
df_from_dict = pd.DataFrame(data_dict)

print(df_from_dict.tail(3))


data_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Creating DataFrame
df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])

print(df_from_list.head(2))

df_csv = pd.read_csv(r"C:\Users\A4952\PycharmProjects\June_automation_batch1\files\sample_csv.csv")

print(df_csv.head(2))