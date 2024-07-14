"""This module is to practice for loop in python
created by Chandan on 14-07-2024"""

'''Question 06:
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''

class_held = int(input("Number of class held: "))
class_attended = int(input("Number of class attended: "))

if (class_attended/class_held)*100 >= 75.0:
    print("Percentage class attended is:",(class_attended/class_held)*100)
    print("Congrats, Allowed to sit exam")
else:
    print("Percentage class attended is:", (class_attended/class_held)*100)
    print("Not Allowed to sit exam")
