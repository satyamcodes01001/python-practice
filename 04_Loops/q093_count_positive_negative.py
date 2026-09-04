"""
Question 93: Count Positive and Negative Numbers

Problem Statement:
Take N integers as input.
Count how many are positive, negative, and zero.

Example:
Input:
5
-2
0
7
-4
3

Output:
Positive: 2
Negative: 2
Zero: 1
"""

# Code :

N=int(input())
p=0
n=0
z=0
while N:
    num=int(input())
    if(num>0):
        p=p+1
    elif(num<0):
        n=n+1
    else:
        z=z+1
    N=N-1

print(f"Positive: {p}")
print(f"Negative: {n}")
print(f"Zero: {z}")
