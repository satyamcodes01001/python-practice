"""
Question 9: Celsius to Fahrenheit

Problem Statement:
Take temperature in Celsius as input.
Convert it to Fahrenheit.

Formula:
F = (C × 9/5) + 32

Example:
Input:
25

Output:
77.0
"""

# Code:

temp=int(input())
fahren=(temp*(9/5))+32
print(f"{fahren:.1f}")

# Concept Clear:

# :2f = Width = 2, Precision = 6 (default).
# :.1f = Always show 1 digit after the decimal.
# :.2f = Always show 2 digits after the decimal.