"""
Question 86: Print Numbers in a Range

Problem Statement:
Take two integers L and R as input.
Print all integers from L to R, inclusive.

Example:
Input:
4
9

Output:
4 5 6 7 8 9
"""

# Code:
a=int(input())
b=int(input())
for i in range(a,b+1):
    print(i,end=" ")

# Concept Clear:-
# range(a, b+1) => range() ka last value include nahi hota, isliye b+1 likhte hain.
# end=" " => Har number ke baad space print karta hai, next line nahi.