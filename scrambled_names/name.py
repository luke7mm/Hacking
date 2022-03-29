# Scrambled names
# Simple program to scramble up your name

import random
from random import shuffle

print('Welcome to the name scrambler!\n\nThis is a simple program which scrambles up your name')

name = input('Please enter your first name here: ')

# Converting str to char and shuffle

char_name = list(name)
random.shuffle(char_name)
result = ''.join(char_name)

print('Your shuffled name is:', result)
