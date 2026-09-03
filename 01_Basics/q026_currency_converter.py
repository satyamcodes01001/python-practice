"""
Question 26: INR to USD Converter

Problem Statement:
Take an amount in Indian Rupees (INR).
Convert it into US Dollars (USD).

Assume:
1 USD = 83 INR

Example:
Input:
830

Output:
10.0 USD
"""

# Code:
 
rs=int(input())
dollars=rs/83
print(f"{dollars:.1f} USD")