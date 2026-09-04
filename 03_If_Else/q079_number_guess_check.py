"""
Question 79: Number Guess Check

Problem Statement:
Assume the secret number is 25.

Take the user's guess as input.

Print:
- Correct
- Too High
- Too Low

Example:
Input:
18

Output:
Too Low
"""

# Code :

n=int(input())
if(n==25):
    print("Correct")
elif(n>25):
    print("Too high")
else:
    print("Too Low")