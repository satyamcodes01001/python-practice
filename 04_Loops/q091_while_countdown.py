"""
Question 91: Countdown Using While Loop

Problem Statement:
Take a positive integer N as input.
Print numbers from N down to 1 using a while loop.

Example:
Input:
5

Output:
5 4 3 2 1
"""

# Code :

n=int(input())

while(n>0):
    print(n,end=" ")
    n=n-1
