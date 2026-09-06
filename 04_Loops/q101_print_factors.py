"""
Question 101: Print All Factors

Problem Statement:
Take a positive integer N as input.
Print all positive factors of N in increasing order.

Example:
Input:
12

Output:
1 2 3 4 6 12
"""

# Code :

n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")

