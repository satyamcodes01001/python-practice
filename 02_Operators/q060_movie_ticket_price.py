"""
Question 60: Movie Ticket Price

Problem Statement:
Take age as input and print the ticket price.

Rules:
Below 5 years : Free
5–17 years    : ₹100
18–59 years   : ₹200
60+ years     : ₹150

Example:
Input:
16

Output:
100
"""

# Code :

age=int(input())
if(age<5):
    print("Free")
elif(age>=5 and age<=17):
    print("100")
elif(age>=18 and age<=59):
    print("200")
else:
    print("150")