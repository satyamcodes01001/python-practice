"""
Question 65: Second Largest of Three Numbers

Problem Statement:
Take three integers as input.
Print the second largest number.

Example:
Input:
15
42
28

Output:
28
"""

# Code :

a=int(input())
b=int(input())
c=int(input())

a=int(input())
b=int(input())
c=int(input())

if((a>b and a<c) or (a>c and a<b)):
    print(a)
elif((b>a and b<c) or (b>c and b<a)):
    print(b)
else:
    print(c)