"""
Question 20: Student ID Card

Problem Statement:
Take the following details as input:

- Name
- Roll Number
- Branch
- College
- CGPA
- Phone Number

Print them in a neatly formatted Student ID Card.

Example Output:

==============================
      STUDENT ID CARD
==============================
Name    : Satyam Seth
Roll No : 25CSE001
Branch  : CSE
College : ABES Engineering College
CGPA    : 8.50
Phone   : 9876543210
==============================
"""

# Code:
name=input()
roll_no=input()
branch=input()
college=input()
cgpa=float(input())
phone=int(input())

print("==============================")
print("      STUDENT ID CARD")
print("==============================")
print(f"Name    : {name}")
print(f"Roll Name    : {roll_no}")
print(f"Branch    : {branch}")
print(f"College    : {college}")
print(f"CGPA    : {cgpa:.2f}")
print(f"Phone    : {phone}")
print("==============================")
