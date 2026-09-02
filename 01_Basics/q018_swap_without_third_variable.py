"""
Question 18: Swap Without Third Variable

Problem Statement:
Take two integers as input.
Swap their values without using a third variable.

Example:
Input:
10
20

Output:
20
10
"""

# Code:

a = int(input())
b = int(input())

a, b = b, a

print(a)
print(b)

# Concept Cleared:

# Python allows multiple assignment:
    # a, b = b, a
    # It swaps both values in a single line without using a third variable.