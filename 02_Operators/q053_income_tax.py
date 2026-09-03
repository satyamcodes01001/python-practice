"""
Question 53: Income Tax

Problem Statement:
Take annual income as input.
Calculate tax using these slabs:

Up to ₹2,50,000        : No Tax
₹2,50,001 - ₹5,00,000  : 5%
₹5,00,001 - ₹10,00,000 : 20%
Above ₹10,00,000       : 30%

Example:
Input:
600000

Output:
120000.0
"""

# Code :
annual=int(input())
if(annual<=250000):
    print("No Tax")
elif(annual>250000 and annual<=500000):
    tax=0.05*annual
    print(f"{tax:.1f}")
elif(annual>500000 and annual<=1000000):
    tax=0.2*annual
    print(f"{tax:.1f}")
else:
    tax=0.3*annual
    print(f"{tax:.1f}")