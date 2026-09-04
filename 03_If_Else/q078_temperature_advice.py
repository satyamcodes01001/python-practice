"""
Question 78: Temperature Advice

Problem Statement:
Take today's temperature as input.

Print:
- Below 15 : Wear a Jacket
- 15–30    : Comfortable Weather
- Above 30 : Stay Hydrated

Example:
Input:
35

Output:
Stay Hydrated
"""

# Code:
temp=int(input())

if(temp<15):
    print("Wear a Jacket")
elif(temp>=15 and temp<=30):
    print("Comfortable Weather")
else:
    print("Stay Hydrated")