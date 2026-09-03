"""
Question 29: Student Result Summary

Problem Statement:
Take the following details as input:

- Name
- Roll Number
- Marks in 5 subjects

Print:

- Name
- Roll Number
- Total Marks
- Percentage

Example Output:

Name       : Satyam
Roll No    : 25CSE001
Total Marks: 432
Percentage : 86.4
"""

# Code:
 
name=input()
rollno=input()

# a,b,c,d,e=map(int,input().split()) jb 1 line mai input dia jaaye tb "I tried this..."

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

total=a+b+c+d+e
per=(total/500)*100
print(f"Name    :{name}")
print(f"Roll No    :{rollno}")
print(f"Total Marks    :{total}")
print(f"Percentage  :{per:.1f}")