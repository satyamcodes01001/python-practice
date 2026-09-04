"""
Question 90: Count Divisors

Problem Statement:
Take a positive integer N.
Count the number of positive divisors of N.

Example:
Input:
12

Output:
6

Explanation:
Divisors of 12 are:
1, 2, 3, 4, 6, 12
"""

n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1

        # Last comma ko handle krne k liye (COndition k saath comma avoid krna)
        if(i==n):
            print(i,end="")
        else:
            print(i,end=",")

# print('\n')      "I tried this"

print()
print(count)

# Concept Clear:

# print() => sirf next line me chala jata hai.
# print('\n') => \n bhi ek newline hai aur print khud bhi newline deta hai, isliye 2 lines ka gap aa jata hai.
# Last comma handled using conditional statements