"""
Question 64: Quadratic Equation Nature

Problem Statement:
Take coefficients a, b and c as input.
Determine whether the roots are:

- Real and Distinct
- Real and Equal
- Imaginary

Use the discriminant:
D = b² - 4ac

Example:
Input:
1
5
6

Output:
Real and Distinct
"""

# Code :

a=int(input())
b=int(input())
c=int(input())

D=b**2-4*a*c

if(D>0):
    print("Real and Distinct")
elif(D==0):
    print("Real and Equal")
else:
    print("Imaginary")