"""
Question 74: State of Water

Problem Statement:
Take temperature in Celsius as input.

Print:
- Ice      : Below 0
- Water    : 0 to 99
- Steam    : 100 or above

Example:
Input:
105

Output:
Steam
"""

# Code :

temp=int(input())
if(temp<0):
    print("Ice")
elif(temp>=0 and temp<100):
    print("Water")
else:
    print("Steam")