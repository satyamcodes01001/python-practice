"""
Question 23: Seconds Converter

Problem Statement:
Take total seconds as input.
Convert them into hours, minutes and seconds.

Example:
Input:
3665

Output:
1 hour 1 minute 5 seconds
"""

# Code :


# Mine Code "I tried this.."
# sec=int(input())
# hrs=sec//60
# minutes=sec//60*60
# print(f"{hrs} hour {minutes} minute {sec} second")

sec = int(input())

hrs=sec//3600
minutes=(sec%3600)//60
seconds=sec%60

print(f"{hrs} hour {minutes} minute {seconds} second")