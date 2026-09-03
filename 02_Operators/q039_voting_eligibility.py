"""
Question 39: Voting Eligibility

Problem Statement:
Take a person's age as input.
Print whether the person is eligible to vote.

Eligibility:
Age >= 18

Example:
Input:
19

Output:
Eligible
"""

# Code :

age=int(input())
if(age>=18):
    print("Elgible")
else:
    print("Not Eligible")