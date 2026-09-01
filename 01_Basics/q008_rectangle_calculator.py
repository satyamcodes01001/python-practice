"""
Question 8: Rectangle Calculator

Problem Statement:
Take the length and width of a rectangle as input.
Print both the area and the perimeter.

Example:
Input:
5
3

Output:
Area: 15
Perimeter: 16
"""

# Code:
length=int(input())
width=int(input())

print(f"Area: {length*width}")
print(f"Perimeter: {2*(length+width)}")