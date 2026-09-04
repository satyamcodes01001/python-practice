"""
Question 69: ATM Withdrawal

Problem Statement:
Take account balance and withdrawal amount as input.

Rules:
- Withdrawal amount must be a multiple of 100.
- Withdrawal amount must not exceed balance.

Print:
- Transaction Successful
- Insufficient Balance
- Invalid Amount

Example:
Input:
5000
1200

Output:
Transaction Successful
"""

# Code :
abal=int(input())
wbal=int(input())

if(abal>=wbal and wbal%100==0):
    print("Transaction Successful")

elif(abal<wbal):
    print("Insufficient Balance")

else:
    print("Invalid Amount")