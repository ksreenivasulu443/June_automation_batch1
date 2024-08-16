# import requests
# url = "https://public.karat.io/content/test/test_log.txt"
# response = requests.get(url)
# log_data = response.text
# log_lines = log_data.splitlines()
# count_block = 0
# release_count = 0
# for i in log_lines:
#     if "Block" in i:
#         count_block = count_block + 1
#     elif "Release" in i:
#         release_count = release_count +1
# print("count_block ", count_block)
# print("release_count", release_count)
#
# #How to remove duplicate from list without using set operator.
# ls = [5,4,1,2,3,1,1,2,5] # [1,2,3,5]
#
# ls = set(ls)
# ls = list(ls)
#
# print("ls after dedup", ls)
#
#
# ls = [5,4,1,2,3,1,1,2,5]
# ls2=[]
# for i in ls:
#     if i not in ls2:
#         ls2.append(i)
#
# ls2.sort()
#
# print(ls2)
#
# #How to count the number of letters in a string.
#
# str2 = 'ETL Automation testing' #- Characters-6
#
# split_out = str2.split(' ')
#
# print("length", len(split_out))
#
# # str2 = 'ETL Automation testing'
# # ETL - 3
# # Automation-10
# # testing-7
#
# str3 = 'Automation' #noitamotuA
#
# print(str3[::-1])
#
# output=''
# for i in str3:
#     output = i + output
#
# print("output",output)
#





url = r"C:\Users\A4952\Desktop\test.txt"

import glob
import os
from pathlib import Path

# Specify the directory you want to iterate through
folder_path = Path('/path/to/your/folder')


folder_path = Path(r"C:\Users\A4952\Desktop\test")

# Iterate through all files in the directory
for file_path in folder_path.iterdir():
    if file_path.is_file():
        #print(f"Found file: {file_path}")
        upper_value = str(file_path).split('\\')[-1].upper()
        print(upper_value)

# out = url.split('\\')[-1].upper()
# print("out", out)

#
#
# file_path = r"C:\Users\A4952\Desktop\online_data.txt"
#
# # Read the log file
# with open(file_path, "r") as file: #r read mode, w - write more, a - append
#     log_data = file.readlines()
#
# # print("log data ", log_data)
# #
# # log_lines = log_data.splitlines()
#
# count_block2=0
# for i in log_data:
#     if "Block" in i:
#         count_block2 +=1
#
# print("count_block2",count_block2)
#
#
#
