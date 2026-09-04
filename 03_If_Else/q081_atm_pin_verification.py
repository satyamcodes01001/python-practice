"""
Question 81: ATM PIN Verification

Problem Statement:
The correct PIN is 1234.

Take a PIN as input.

Print:
- Access Granted
- Incorrect PIN

Example:
Input:
1234

Output:
Access Granted
"""

# Code :
pin=int(input())

if(pin==1234):
    print("Access Granted")
else:
    print("Access Denied")