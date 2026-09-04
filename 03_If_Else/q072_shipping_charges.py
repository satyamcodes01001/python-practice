"""
Question 72: Shipping Charges

Problem Statement:
Take the order amount as input.

Rules:
- ₹1000 or more : Free Shipping
- Otherwise     : ₹80 Shipping

Print the final amount including shipping.

Example:
Input:
750

Output:
830
"""

# Code :
amt=int(input())
if(amt>=1000):
    print(amt)
else:
    print(amt+80)