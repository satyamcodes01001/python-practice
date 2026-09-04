"""
Question 82: Weekend or Weekday

Problem Statement:
Take a day name as input.

Print:
- Weekend → Saturday or Sunday
- Weekday → Monday to Friday

Example:
Input:
Sunday

Output:
Weekend
"""

# Code :
day=input()
day=day.lower()

if(day=="saturday" or day=="sunday"):
    print("Weekend")
else:
    print("Weekday")