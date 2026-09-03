"""
Question 48: Age Category

Problem Statement:
Take age as input.
Print the category using these rules:

0-12   : Child
13-19  : Teen
20-59  : Adult
60+    : Senior Citizen

Example:
Input:
18

Output:
Teen
"""

# Code:

age=int(input())
if(age<0):
    print("Invalid Age")
elif(age>=0 and age<=12):
    print("Child")
elif(age>=13 and age<=19):
    print("Teen")
elif(age>=20 and age<=59):
    print("Adult")
else:
    print("Senior Citizen")