"""
Question 57: Exam Eligibility

Problem Statement:
Take the attendance percentage as input.
A student is eligible for the exam only if attendance is 75% or above.

Example:
Input:
82

Output:
Eligible
"""

# Code:

attend=int(input())
if(attend>=75):
    print("Elgible")
else:
    print("Not Eligible")