"""
Question 40: Grade Calculator

Problem Statement:
Take percentage as input.
Print the grade using the following rules:

90-100 : A
80-89  : B
70-79  : C
60-69  : D
Below 60 : F

Example:
Input:
86

Output:
B
"""

# Code:

per=int(input())
if(per>=90 and per<=100):
    print("A")
elif(per>=80 and per<90):
    print("B")
elif(per>=70 and per<80):
    print("C")
elif(per>=60 and per<70):
    print("D")
else:
    print("F")