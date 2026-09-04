"""
Question 73: Scholarship Eligibility

Problem Statement:
Take percentage and annual family income as input.

Rules:
- Percentage must be 85 or above.
- Income must be ₹3,00,000 or less.

Print:
- Scholarship Approved
- Scholarship Not Approved

Example:
Input:
90
250000

Output:
Scholarship Approved
"""

# Code :
per=int(input())
income=int(input())

if(per>=85 and income<=300000):
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")