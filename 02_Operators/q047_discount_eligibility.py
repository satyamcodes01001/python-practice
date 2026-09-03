"""
Question 47: Discount Eligibility

Problem Statement:
Take the shopping amount as input.
If the amount is 1000 or more, print "Discount Applied".
Otherwise print "No Discount".

Example:
Input:
1500

Output:
Discount Applied
"""

# Code :

amt=int(input())
if(amt>=1000):
    print("Discount Applied")
else:
    print("No Discount")