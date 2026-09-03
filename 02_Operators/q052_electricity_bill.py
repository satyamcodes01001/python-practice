"""
Question 52: Electricity Bill

Problem Statement:
Take the number of electricity units consumed as input.
Calculate the bill using these rates:

First 100 units    : ₹5/unit
Next 100 units     : ₹7/unit
Above 200 units    : ₹10/unit

Example:
Input:
250

Output:
1700
"""

# Code :
n=int(input())
if(n<=100):
    print(n*5)
elif(n<=200):
    print((100*5)+((n-100)*7))
else:
    print((100*5)+(100*7)+(n-200)*10)