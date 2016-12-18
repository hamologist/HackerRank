import fileinput
import string

line = fileinput.input()[0].strip()
words = 1

for char in line:
    if char in string.ascii_uppercase:
        words += 1

print(words)
