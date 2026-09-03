"""
Question 32: Positive, Negative or Zero

Problem Statement:
Take an integer as input.
Print whether it is Positive, Negative or Zero.

Example:
Input:
-5

Output:
Negative
"""

# Code :

n=int(input())
if(n>0):
    print("Positive")
elif(n<0):
    print("Negative")
else:
    print("Zero")