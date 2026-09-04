"""
Question 68: Character Classifier

Problem Statement:
Take a single character as input.
Print whether it is:

- Vowel
- Consonant
- Digit
- Special Character

Example:
Input:
@

Output:
Special Character
"""

# Code :

ch=input()
# Mine........
# ch.lower()            "Ye original ch ko change nahi karta"
# if("aeiou" in ch):    "Vowel check ulta hai..."
#     print("Vowel")
# elif(ch.isdigit()):
#     print("Digit")
# elif(ch>='a' and ch<='z'):
#     print("Consonant")
# else:
#     print("Special Character")

# Corrected version:

ch=ch.lower()
if(ch in "aeiou"):
    print("Vowel")
elif(ch.isdigit()):
    print("Digit")
elif(ch>='a' and ch<='z'):
    print("Consonant")
else:
    print("Special Character")