"""
Question 19: Minutes to Hours

Problem Statement:
Take the total number of minutes as input.
Convert it into hours and remaining minutes.

Example:
Input:
135

Output:
2 hours 15 minutes
"""

# Code:

minutes=int(input())
hrs=minutes//60
rem=minutes%60
print(f"{hrs} hours {rem} minutes")
