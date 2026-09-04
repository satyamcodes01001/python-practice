"""
Question 95: First Multiple

Problem Statement:
Take two integers N and K as input.
Starting from 1, find and print the first number that is divisible by both N and K.

Example:
Input:
6
8

Output:
24
"""

# Code :
N=int(input())
K=int(input())

# Mistake : HCF nikaalne ka code likha hu ->(First common divisoor nikaal rhaa)
# for i in range(2,max(N+1,K+1)):
#     if(N%i==0 and K%i==0):
#         print(i)
#         break


for i in range(2,N*K+1):
    if(i%N==0 and i%K==0):
        print(i)
        break

# Concept/Doubts Clear:

# N % i == 0 → i N ka factor (divisor) hota hai.
# i % N == 0 → i N ka multiple hota hai.
# Divisor aur Multiple ki condition opposite hoti hai.
# LCM hamesha N × K se bada nahi hota, isliye N*K tak search kar sakte hain.
# Pehla common multiple = LCM (Least Common Multiple).

# % ka matlab hai "left ko right se divide karo."
        # 12 % 3 → 12 ko 3 se divide → 3 factor.
        # 24 % 6 → 24 ko 6 se divide → 24 multiple.