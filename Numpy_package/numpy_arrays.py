import numpy as np
import pandas as pd
from pandasql import sqldf

#create array
arr = np.array([1,2,'string']) #Result --> all values are coverted to String as it numpy is homogeneous in nature
print("arr value is:",arr)
print("Dimention of arr is:",arr.ndim)

arr1 = np.array([[1,2,3],[4,5,6]])
print("arr1 value is:",arr1)
print("Dimention of arr1 is:",arr1.ndim) #2 dimension array

#array slicing
#first index is for ROW, 2nd index is for position of element (column) in that row, index starts from "0"
print("arr1[1][2] is:",arr1[1][2]) #Result --> 6
print("arr1[0][1] is:",arr1[0][1]) #Result --> 2

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("arr2 value is:",arr2)
print("Dimention of arr2 is:",arr2.ndim) #2 Dimension array
print("arr2[1][2] is:",arr2[1][2])
print("arr2[2][1] is:",arr2[2][1])
