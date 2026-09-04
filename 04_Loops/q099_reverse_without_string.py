"""
Question 99: Reverse Without Using String Conversion

Problem Statement:
Take a positive integer as input.
Reverse the number without converting it into a string.

You must solve this using arithmetic operations and a loop.

Example:
Input:
12345

Output:
54321
"""

# Code :

n=int(input())
sum=0
while(n>0):
    digit=n%10
    sum=(sum*10)+digit
    n//=10
print(sum)