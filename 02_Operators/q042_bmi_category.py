"""
Question 42: BMI Category

Problem Statement:
Take weight (kg) and height (m) as input.
Calculate BMI and print the category.

Categories:
Below 18.5      : Underweight
18.5 - 24.9     : Normal
25 - 29.9       : Overweight
30 or above     : Obese

Example:
Input:
70
1.75

Output:
Normal
"""

# Code :
wt=float(input())
ht=float(input())
bmi=wt/(ht*ht)
if(bmi<18.8):
    print("Underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("Normal")
elif(bmi>=25 and bmi<=29.9):
    print("Overweight")
else:
    print("Obese")