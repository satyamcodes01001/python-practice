"""
Question 75: Traffic Signal

Problem Statement:
Take the traffic light color as input.

Rules:
- Red    → Stop
- Yellow → Wait
- Green  → Go

Example:
Input:
Yellow

Output:
Wait
"""

# Code :

l=input()
l=l.lower()

if(l=="red"):
    print("Stop")
elif(l=="yellow"):
    print("Wait")
elif(l=="green"):
    print("Go")
else:
    print("Invalid Signal")