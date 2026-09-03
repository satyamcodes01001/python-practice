"""
Question 22: Days Converter

Problem Statement:
Take the total number of days as input.
Convert them into years, months and remaining days.

Assume:
1 year = 365 days
1 month = 30 days

Example:
Input:
400

Output:
Years : 1
Months: 1
Days  : 5
"""

# Code:

days=int(input())
year=days//365
month=(days-(year*365))//30
remdays=days-((year*365)+(month*30))
print(f"Years: {year}")
print(f"Months: {month}")
print(f"Days: {remdays}")

