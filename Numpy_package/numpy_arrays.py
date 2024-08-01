import numpy as np
import pandas as pd

from pandasql import sqldf

arr = np.array([1,2,3,3.4,'str', True])

#str>float>int>bool

print("arr is ", arr)
print("arr type is", type(arr))

print("arr[0] type", arr[0], type(arr[0]))
print("arr[3] type", arr[3], type(arr[3]))
print("arr[4] type", arr[4], type(arr[4]))

print("dimention", arr.ndim)

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("arr2", arr2)
print("dimention", arr2.ndim)

print("arr2[0][1]",arr2[0][1])

print("arr2[0:2]",arr2[0:2][0:2]) # [rows][col]






