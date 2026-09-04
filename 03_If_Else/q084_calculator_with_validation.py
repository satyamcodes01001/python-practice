"""
Question 84: Calculator with Validation

Problem Statement:
Take two numbers and an operator (+, -, *, /).

Perform the operation.

Rules:
- If division by zero occurs, print "Cannot Divide by Zero".
- If the operator is invalid, print "Invalid Operator".

Example:
Input:
10
/
0

Output:
Cannot Divide by Zero
"""

# Code :
a=int(input())
op=input()
b=int(input())

match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        if b==0:
            print("Cannot Divide By Zero")
        else:
            print(a/b)
    case _:
        print("Invalid Operator")