"""
Question 70: Login System

Problem Statement:
Take username and password as input.

Rules:
Username : admin
Password : python123

Print:
- Login Successful
- Incorrect Password
- User Not Found

Example:
Input:
admin
wrong123

Output:
Incorrect Password
"""

# Code :

uname=input()
key=input()

if(uname=="admin" and key=="python123"):
    print("Login Successful")
elif(uname=="admin" and key!="python123"):
    print("Incorrect Password")
else:
    print("User Not Found")