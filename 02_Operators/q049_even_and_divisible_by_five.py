"""
Question 49: Even and Divisible by 5

Problem Statement:
Take an integer as input.
Print "Yes" if the number is both even and divisible by 5.
Otherwise print "No".

Example:
Input:
20

Output:
Yes
"""

# Code :
n=int(input())
if(n%2==0 and n%5==0):
    print("Yes")
else:
    print("No")