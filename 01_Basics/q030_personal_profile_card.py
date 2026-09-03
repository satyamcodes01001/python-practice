"""
Question 30: Personal Profile Card

Problem Statement:
Take the following details as input:

- Name
- Age
- College
- Branch
- City
- Phone Number

Print them in a neatly formatted profile card.

Example Output:

==============================
      PERSONAL PROFILE
==============================
Name    : Satyam Seth
Age     : 18
College : ABES Engineering College
Branch  : CSE
City    : Ghaziabad
Phone   : 9876543210
==============================
"""

# Code :

name=input()
age=int(input())
college=input()
branch=input()
city=input()
phoneno=int(input())

print("==============================")
print("      PERSONAL PROFILE")
print("==============================")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"College : {college}")
print(f"Branch  : {branch}")
print(f"City    : {city}")
print(f"Phone   : {phoneno}")
