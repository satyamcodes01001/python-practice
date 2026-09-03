"""
Question 51: Calculator

Problem Statement:
Take two numbers and an operator (+, -, *, /, %) as input.
Perform the corresponding operation and print the result.

Example:
Input:
10
*
5

Output:
50
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
            print("Invalid Division")
        else:
            print(a/b)
    case '%':
        if b==0:
            print("Invalid Division")
        else:
            print(a%b)
    case _:
        print("Invalid Operator")

# Concept Clears:

# Python me _ ek wildcard hai. Iska matlab hai "kuch bhi ho, match kar lo." Isliye case _: hamesha last me likhte hain