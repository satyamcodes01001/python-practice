"""
Question 85: Bank Minimum Balance

Problem Statement:
Take account balance as input.

Rules:
- Below ₹1000 → Low Balance
- ₹1000 or more → Balance OK

Example:
Input:
850

Output:
Low Balance
"""

# Code :
bal=int(input())
if(bal<1000):
    print("Low Balance")
else:
    print("Balance OK")