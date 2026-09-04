"""
Question 97: Product of Digits

Problem Statement:
Take a positive integer as input.
Calculate and print the product of all its digits.

Example:
Input:
1234

Output:
24
"""

# Code :

n=int(input())
prod=1
while(n>0):
    digit=n%10
    prod=prod*digit
    n//=10
print(prod)