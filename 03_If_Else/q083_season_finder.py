"""
Question 83: Season Finder

Problem Statement:
Take a month number (1–12) as input.
Print the season.

Rules:
- Dec, Jan, Feb → Winter
- Mar, Apr, May → Summer
- Jun, Jul, Aug → Monsoon
- Sep, Oct, Nov → Autumn

Example:
Input:
7

Output:
Monsoon
"""

# Code :
n=int(input())

if(n>=1 and n<=12):
    if(n==1 or n==2 or n==12):
        print("Winter")
    elif(n>=3 and n<=5):
        print("Summer")
    elif(n>=6 and n<=8):
        print("Monsoon")
    else:
        print("Autumn")
else:
    print("Invalid Month")
