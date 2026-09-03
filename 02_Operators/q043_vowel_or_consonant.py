"""
Question 43: Vowel or Consonant

Problem Statement:
Take a single alphabet as input.
Print whether it is a Vowel or Consonant.

Example:
Input:
a

Output:
Vowel
"""

# Code:

ch=input()
ch.lower()


# if('a' or 'e' or 'i' or 'u'  in ch):
#     print("Vowel")
# else:
#     print("Consonants")

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# Concept Learn:
# Ek character ko multiple values se compare karna ho to in use karo (ch in "aeiou")