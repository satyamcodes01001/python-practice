"""
Question 35: Largest of Three Numbers

Problem Statement:
Take three integers as input.
Print the largest number.

Example:
Input:
10
45
32

Output:
45
"""

# Code:

a=int(input())
b=int(input())
c=int(input())
if(a>=b and a>=c):
    print(a)
elif(b>=a and b>=c):
    print(b)
else:
    print(c)