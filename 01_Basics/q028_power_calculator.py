"""
Question 28: Power Calculator

Problem Statement:
Take two integers as input:

- Base
- Exponent

Print the value of Base raised to the power Exponent.

Example:
Input:
2
5

Output:
32
"""

# Code:

base=int(input())
exp=int(input())
# power=pow(2,5)     I tried this which is hardcore or we can say brutful
power=base**exp
print(power)