import pandas as pd

series = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(series)
print("series['a']",series['a']) #Result --> 1
print("series['d']",series['d']) #Result --> 4

#instead of index values, we can provide our own indexes, otherwise it create own index values
