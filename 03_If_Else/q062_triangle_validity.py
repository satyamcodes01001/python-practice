"""
Question 62: Triangle Validity

Problem Statement:
Take the lengths of three sides as input.
Print whether a valid triangle can be formed.

Rule:
The sum of any two sides must be greater than the third side.

Example:
Input:
3
4
5

Output:
Valid Triangle
"""

# Code :


a=int(input())
b=int(input())
c=int(input())

if(a+b>c and b+c>a and a+c>b):
    print("Valid Triangle")
else:
    print("Invalid Triangle")