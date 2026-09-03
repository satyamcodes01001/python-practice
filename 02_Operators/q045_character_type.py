"""
Question 45: Character Type

Problem Statement:
Take a single character as input.
Print whether it is:

- Alphabet
- Digit
- Special Character

Example:
Input:
7

Output:
Digit
"""

# Code :

a=input()
if(a.isalpha()):
    print("Alphabet")
elif(a.isdigit()):
    print("Digit")
else:
    print("Special Character")