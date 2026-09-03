"""
Question 59: Number Range

Problem Statement:
Take an integer as input.
Print whether it lies between 1 and 100 (inclusive).

Example:
Input:
78

Output:
Inside Range
"""

# Code :

n=int(input())
if(n>=1 and n<=100):
    print("Inside Range")
else:
    print("Not Inside Range")