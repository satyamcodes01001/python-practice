"""
Question 7: Area of a Circle

Problem Statement:
Take the radius of a circle as input.
Print its area using the value of pi from Python's math module.

Example:
Input:
7

Output:
153.94
"""

# Code:

import math
pi=math.pi
r=int(input())
value=pi*r*r
# print(round(value, 2)) "I tried to use this.."
print(f"{value:.2f}")

# Concept Clear:

# round(value, 2)=rounds the number to 2 decimal places. It may not always display two digits after the decimal point
# f"{value:.2f}"=always displays exactly 2 digits after the decimal point, even if they are zeros