"""
Question 58: Password Strength

Problem Statement:
Take a password as input.
Print:

- Strong → length is 8 or more
- Weak → length is less than 8

Example:
Input:
python123

Output:
Strong
"""

# Code:

key=input()

if(len(key)>=8):
    print("Strong")
else:
    print("Weak")