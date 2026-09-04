"""
Question 92: Sum Until Zero

Problem Statement:
Keep taking integers as input and calculate their sum.
Stop taking input when the user enters 0.

The final sum should be printed.

Example:
Input:
5
10
7
0

Output:
22
"""

# Code :

n=1
Sum=0
while(n):
    n=int(input())
    Sum=Sum+n

print(Sum)