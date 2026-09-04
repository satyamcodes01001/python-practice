"""
Question 100: Sum of a Series

Problem Statement:
Take N as input and calculate:

1 + 2 + 3 + ... + N

Do not use the direct mathematical formula.
Use a loop.

Example:
Input:
10

Output:
55
"""

# Code:

n=int(input())
Sum=0
for i in range(1,n+1):
    Sum+=i
print(Sum)