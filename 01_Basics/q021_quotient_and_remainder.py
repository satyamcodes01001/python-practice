"""
Question 21: Quotient and Remainder

Problem Statement:
Take two integers as input and print both the quotient and the remainder.

Example:
Input:
17
5

Output:
Quotient: 3
Remainder: 2
"""

# Code :

a=int(input())
b=int(input())

quotient=a//b
rem=a%b

print(f"Quotient:{quotient}")
print(f"Remainder:{rem}")