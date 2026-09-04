"""
Question 63: Triangle Type

Problem Statement:
Take three sides of a triangle as input.
Print the type of triangle.

Rules:
- Equilateral
- Isosceles
- Scalene

Example:
Input:
5
5
8

Output:
Isosceles
"""

# Code :

a=int(input())
b=int(input())
c=int(input())

if(a+b>c and b+c>a and a+c>b):
    if(a==b and b==c and c==a):
        print("Equilateral")
    elif(a==b or b==c or c==a):
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid Triangle")