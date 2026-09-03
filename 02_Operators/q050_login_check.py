"""
Question 50: Login Check

Problem Statement:
Take a username and password as input.

Rules:
Username must be "admin"
Password must be "python123"

If both are correct, print "Login Successful".
Otherwise print "Invalid Credentials".

Example:
Input:
admin
python123

Output:
Login Successful
"""

# Code :

uname=input()
password=input()
if(uname=="admin" and password=="python123"):
    print("Login Successful")
else:
    print("Invalid Credentials")
