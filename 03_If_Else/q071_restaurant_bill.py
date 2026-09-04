"""
Question 71: Restaurant Bill

Problem Statement:
Take the total bill amount as input.

Apply discount using these rules:
- ₹500 or less      : No Discount
- ₹501 – ₹1000      : 10% Discount
- Above ₹1000       : 20% Discount

Print the final payable amount.

Example:
Input:
1200

Output:
960.0
"""

# Code :
bill=int(input())

if(bill<=500):
    print(bill)
elif(bill>500 and bill<=1000):
    print(f"{bill-bill*0.1:.1f}")
else:
    print(f"{bill-bill*0.2:.1f}")
