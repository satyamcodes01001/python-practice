"""
Question 41: Profit or Loss

Problem Statement:
Take Cost Price (CP) and Selling Price (SP) as input.
Print whether there is a Profit, Loss, or No Profit No Loss.

Example:
Input:
100
120

Output:
Profit
"""

# Code:
cp=int(input())
sp=int(input())
if(sp>cp):
    print("Profit")
elif(sp<cp):
    print("Loss")
else:
    print("No Profit No Loss")