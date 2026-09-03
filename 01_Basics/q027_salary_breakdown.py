"""
Question 27: Salary Breakdown

Problem Statement:
Take an employee's basic salary.
Calculate:

- HRA = 20% of Basic Salary
- DA = 10% of Basic Salary
- Gross Salary = Basic + HRA + DA

Example:
Input:
50000

Output:
HRA: 10000
DA: 5000
Gross Salary: 65000
"""

# Code:

sal=int(input())
hra=0.2*sal
da=0.1*sal
gross=sal+hra+da
print(f"HRA : {hra:.0f}")
print(f"DA : {da:.0f}")
print(f"Gross Salary : {gross:.0f}")