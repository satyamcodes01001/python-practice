"""
Question 89: Count Divisible Numbers

Problem Statement:
Take N as input.
Count how many numbers from 1 to N are divisible by 3.

Example:
Input:
10

Output:
3
"""
# Code :

n=int(input())
count=0
for i in range(1,n+1):
    if(i%3==0):
        count=count+1

print(count)