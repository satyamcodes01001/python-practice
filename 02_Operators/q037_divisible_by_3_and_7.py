"""
Question 37: Divisible by 3 and 7

Problem Statement:
Take an integer as input.
Print whether it is divisible by both 3 and 7.

Example:
Input:
42

Output:
Yes
"""

# Code:
n=int(input())
if(n%3==0 and n%7==0):
    print("Yes")
else:
    print("No")