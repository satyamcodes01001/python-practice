"""
Question 87: Sum of a Range

Problem Statement:
Take two integers L and R as input.
Calculate and print the sum of all integers from L to R, inclusive.

Example:
Input:
3
7

Output:
25
"""

# Code :

a=int(input())
b=int(input())
sum=0
for i in range(a,b+1):
    sum+=i

print(sum)