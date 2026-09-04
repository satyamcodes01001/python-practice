"""
Question 98: Digit Frequency

Problem Statement:
Take a positive integer N as input.
Take another digit D (0-9) as input.
Count how many times digit D occurs in N.

Example:
Input:
122321
2

Output:
3
"""

# Code :

n=int(input())
d=int(input())

count=0
while(n>0):
    digit=n%10
    if(digit==d):
        count=count+1
    n//=10

print(count)