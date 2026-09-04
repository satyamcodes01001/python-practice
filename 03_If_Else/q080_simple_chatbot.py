"""
Question 80: Simple Chatbot

Problem Statement:
Take one word as input.

Rules:
- "hi"    → Hello!
- "bye"   → Goodbye!
- "thanks"→ You're Welcome!
- Anything else → I don't understand.

Example:
Input:
hi

Output:
Hello!
"""

# Code :
wd=input()
if(wd=="hi"):
    print("Hello!")
elif(wd=="bye"):
    print("Goodbye!")
elif(wd=="thanks"):
    print("You're Welcome!")
else:
    print("I don't understand.")