"""
Question 38: Leap Year

Problem Statement:
Take a year as input.
Print whether it is a Leap Year.

Rules:
- Divisible by 400 → Leap Year
- Divisible by 100 → Not Leap Year
- Divisible by 4 → Leap Year
- Otherwise → Not Leap Year

Example:
Input:
2024

Output:
Leap Year
"""

# Code:

year=int(input())

if(year%400==0):
    print("Leap Year")
elif(year%100==0):
    print("Not Leap Year")
elif(year%4==0):
    print("Leap Year")
else:
    print("Not Leap Year")