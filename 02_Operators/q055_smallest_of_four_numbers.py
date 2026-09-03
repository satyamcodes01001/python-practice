"""
Question 55: Smallest of Four Numbers

Problem Statement:
Take four integers as input.
Print the smallest number.

Example:
Input:
9
3
12
5

Output:
3
"""

# Code :

a=int(input())
b=int(input())
c=int(input())
d=int(input())

print(a if a<=b and a<=c and a<=d else b if b<=a and b<=c and b<=d else c if c<=a and c<=b and c<=d else d) 

# COncept Clear :
    # nested ternary operator used