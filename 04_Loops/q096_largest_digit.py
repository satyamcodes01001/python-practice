"""
Question 96: Largest Digit

Problem Statement:
Take a positive integer as input.
Find and print its largest digit.

Example:
Input:
58321

Output:
8
"""

# Code :

n=int(input())
largest=0
while(n>0):
    digit=n%10
    if(digit>largest):
        largest=digit
    n//=10
print(largest)
