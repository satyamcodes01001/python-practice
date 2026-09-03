"""
Question 25: Shopping Bill

Problem Statement:
Take the price of one item and the quantity purchased.
Print the total bill.

Example:
Input:
120
3

Output:
Total Bill: 360
"""

# Code:

item=int(input())
quantity=int(input())

total_bill=item*quantity
print(f"Total Bill: {total_bill}")