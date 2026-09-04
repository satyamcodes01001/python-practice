"""
Question 67: Days in a Month

Problem Statement:
Take a month number (1-12) as input.
Print the number of days in that month.

Assume February has 28 days.

Example:
Input:
2

Output:
28
"""

# Code :

n=int(input())

if(n==2):
    print("28")
elif(n==4 or n==6 or n==9 or n==11):
    print("30")
else:
    print("31")