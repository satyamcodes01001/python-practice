"""
Question 94: Skip Multiples of 3

Problem Statement:
Take N as input.
Print numbers from 1 to N, but skip all numbers divisible by 3.

Example:
Input:
10

Output:
1 2 4 5 7 8 10
"""

# Code :
N=int(input())
for i in range(1,N+1):
    if(i%3==0):
        continue
    print(i,end=" ")
