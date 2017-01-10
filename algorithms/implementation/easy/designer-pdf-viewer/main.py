import fileinput
from string import ascii_lowercase

lines = [line.strip() for line in fileinput.input()]
letter_heights = {
    letter: int(letter_height)
    for letter, letter_height 
    in zip(ascii_lowercase, lines[0].split(' '))
}
text = lines[1]

print(len(text) * max([letter_heights[letter] for letter in text]))
