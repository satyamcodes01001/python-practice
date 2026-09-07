"""
Question 102: Count Prime Numbers

Problem Statement:
Take an integer N as input.
Count how many prime numbers exist from 1 to N.

Example:
Input:
10

Output:
4

Explanation:
Prime numbers are:
2, 3, 5, 7
"""

# Code:

n=int(input())
count=0

# 2 se N tak har number ko check karenge
for num in range(2,n+1):

    is_prime=True  # Har naye number ke liye maan lo prime hai

    # 2 se num-1 tak divide karke check karo
    for i in range(2,num):
        if(num%i==0):
            is_prime=False  # Divisible mila to prime nahi
            break

    # Agar prime hai to count badha do
    if(is_prime):
        count+=1

print(count)