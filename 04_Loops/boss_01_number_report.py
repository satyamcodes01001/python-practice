"""
Boss Challenge: Number Report

Problem Statement:
Take an integer N as input.

For all numbers from 1 to N, calculate:

1. Total numbers
2. Sum
3. Number of even numbers
4. Number of odd numbers
5. Sum of even numbers
6. Sum of odd numbers
7. Largest number

Example:
Input:
10

Output:
Total Numbers: 10
Sum: 55
Even Count: 5
Odd Count: 5
Even Sum: 30
Odd Sum: 25
Largest: 10
"""

# Code :

n=int(input())

totalno=0
Sum=0
evencount=0
oddcount=0
evensum=0
oddsum=0
largest=n

for i in range(1,n+1):

    totalno=totalno+1
    Sum+=i

    if(i%2==0):
        evencount=evencount+1
        evensum+=i
    else:
        oddcount=oddcount+1
        oddsum+=i

print(f"Total Numbers: {totalno}")
print(f"Sum: {Sum}")
print(f"Even Count: {evencount}")
print(f"Odd Count: {oddcount}")
print(f"Even Sum: {evensum}")
print(f"Odd Sum: {oddsum}")
print(f"Largest :{largest}")