# Simple regex search

import re

f = open("jfk_moon.txt", "r")

words = re.findall("We choose to go to the moon", f.read())

print(words)

