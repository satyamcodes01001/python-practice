"""
Question 76: Movie Ticket Discount

Problem Statement:
Take age and ticket price as input.

Rules:
- Below 12 years : 50% Discount
- 60 years or above : 30% Discount
- Otherwise : No Discount

Print the final ticket price.

Example:
Input:
10
200

Output:
100.0
"""

# Code :
age=int(input())
price=int(input())

if(age<12):
    print(price*0.5)
elif(age>=60):
    print(price*0.7)
else:
    print(float(price))