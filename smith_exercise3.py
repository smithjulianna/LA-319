#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

number = random.randrange(1, 500)
guesses = 0
guess = int(input("Please try to guess the randomized number between 1 & 500: "))

while guess != number:
    guesses += 1
    if guess > number:
        print(guess, "is too high of a number.")
    if guess < number:
        print(guess, "is too low of a number.")
    guess = int(input("Oops! Guess again:" ))
    
print("Great, you got it in", guesses,  "guesses!")


# In[ ]:




