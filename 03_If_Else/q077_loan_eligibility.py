"""
Question 77: Loan Eligibility

Problem Statement:
Take age and monthly salary as input.

Rules:
- Age must be between 21 and 60.
- Salary must be ₹25,000 or more.

Print:
- Eligible
- Not Eligible

Example:
Input:
28
40000

Output:
Eligible
"""

# Code :
age=int(input())
salary=int(input())
if(age>=21 and age<=60 and salary>=25000):
    print("Eligible")
else:
    print("Not Eligible")