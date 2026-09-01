"""
Question 10: Simple Interest

Problem Statement:
Take Principal (P), Rate (R), and Time (T) as input.
Calculate and print the Simple Interest.

Formula:
SI = (P × R × T) / 100

Example:
Input:
1000
5
2

Output:
100.0
"""

# Code:

P=int(input())
R=int(input())
T=int(input())

SI=(P*R*T)/100
print(f"{SI:.1f}")


