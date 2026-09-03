"""
Question 24: Percentage Calculator

Problem Statement:
Take marks of five subjects as input.
Calculate the total marks and percentage.

Example:
Input:
80
75
90
85
70

Output:
Total: 400
Percentage: 80.0
"""

# Code:

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

total=a+b+c+d+e
per=(total/500)*100

print(f"Total: {total}")
print(f"Percentage: {per:.1f}")