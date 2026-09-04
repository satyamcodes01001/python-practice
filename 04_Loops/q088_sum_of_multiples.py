"""
Question 88: Sum of Multiples

Problem Statement:
Take N as input.
Calculate the Sum of all numbers from 1 to N that are divisible by both 3 and 5.

Example:
Input:
30

Output:
45
"""
# Code :

n=int(input())
Sum=0
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        Sum+=i

print(Sum)