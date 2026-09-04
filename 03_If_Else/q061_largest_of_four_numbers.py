"""
Question 61: Largest of Four Numbers

Problem Statement:
Take four integers as input.
Print the largest number.

Example:
Input:
12
45
8
31

Output:
45
"""

# Code:

a=int(input())
b=int(input())
c=int(input())
d=int(input())

if(a>=b and a>=c and a>=d):
    print(a)
elif(b>=a and b>=c and b>=d):
    print(b)
elif(c>=a and c>=b and c>=d):
    print(c)
else:
    print(d)