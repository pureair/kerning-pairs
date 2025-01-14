'''
Data is in the form:
letters = {
    " ": ((-1, -1, -1, -1, -1), (-1, -1, -1, -1, -1)),  # 32
    "!": ((0, 0, 0, 0, -1), (0, 0, 0, 0, -1)),  # 33
    '"': ((1, 1, -1, -1, -1), (1, 1, -1, -1, -1)),  # 34
}

let's call each item: "letter": (leftside, rightside)
write a python script to group all letter by its rightside (ie. if rightside is the same then put into same group) and output like:
'
Group 1
a b c 

Group 2
e f
'

then group all letter by its leftside and output again.

then, use only the first letter in each group, list all combination of rightside_groups + leftside_groups. when listing, add no space, add new line every 15 pairs (ie, 30 characters).
'''

import itertools

letters = {
    "A": ((-1, -1, -1, 1, -1), (-1, -1, -1, 1, -1)),
    "B": ((0, 0, 0, 0, -1), (-1, -1, 1, -1, -1)),
    "C": ((-1, 1, 1, -1, -1), (-1, -1, -1, -1, -1)),
    "D": ((0, 0, 0, 0, -1), (-1, 1, 1, -1, -1)),
    "E": ((0, 0, 0, 0, -1), (1, 1, -1, 1, -1)),
    "F": ((0, 0, 0, 0, -1), (1, 1, -1, -1, -1)),
    "G": ((-1, 1, 1, -1, -1), (-1, 0, 0, 0, -1)),
    "H": ((0, 0, 0, 0, -1), (0, 0, 0, 0, -1)),
    "I": ((0, 0, 0, 0, -1), (0, 0, 0, 0, -1)),
    "J": ((-1, -1, -1, 1, -1), (0, 0, 0, -1, -1)),
    "K": ((0, 0, 0, 0, -1), (1, -1, -1, 1, -1)),
    "L": ((0, 0, 0, 0, -1), (-1, -1, -1, 1, -1)),
    "M": ((0, 0, 0, 0, -1), (0, 0, 0, 0, -1)),
    "N": ((0, 0, 0, 0, -1), (0, 0, 0, 0, -1)),
    "O": ((-1, 1, 1, -1, -1), (-1, 1, 1, -1, -1)),
    "P": ((0, 0, 0, 0, -1), (-1, 1, -1, -1, -1)),
    "Q": ((-1, 1, 1, -1, -1), (-1, 1, 1, 1, -1)),
    "R": ((0, 0, 0, 0, -1), (-1, 1, -1, 1, -1)),
    "S": ((-1, 0, 0, -1, -1), (-1, 0, 0, -1, -1)),
    "T": ((1, -1, -1, -1, -1), (1, -1, -1, -1, -1)),
    "U": ((0, 0, 0, -1, -1), (0, 0, 0, -1, -1)),
    "V": ((1, -1, -1, -1, -1), (1, -1, -1, -1, -1)),
    "W": ((1, -1, -1, -1, -1), (1, -1, -1, -1, -1)),
    "X": ((1, -1, -1, 1, -1), (1, -1, -1, 1, -1)),
    "Y": ((1, -1, -1, -1, -1), (1, -1, -1, -1, -1)),
    "Z": ((1, -1, -1, 1, -1), (1, -1, -1, 1, -1)),
    "a": ((-1, -1, 0, -1, -1), (-1, -1, 0, 0, -1)),
    "b": ((0, 0, 0, 0, -1), (-1, -1, 1, -1, -1)),
    "c": ((-1, -1, 1, -1, -1), (-1, -1, -1, -1, -1)),
    "d": ((-1, -1, 1, -1, -1), (0, 0, 0, 0, -1)),
    "e": ((-1, -1, 1, -1, -1), (-1, -1, 1, -1, -1)),
    "f": ((-1, 1, -1, -1, -1), (1, 1, -1, -1, -1)),
    "g": ((-1, -1, 1, 0, -1), (-1, 0, 0, 0, -1)),
    "h": ((0, 0, 0, 0, -1), (-1, -1, 0, 0, -1)),
    "i": ((0, 0, 0, 0, -1), (0, 0, 0, 0, -1)),
    "j": ((0, 0, 0, 0, 1), (0, 0, 0, 0, -1)),
    "k": ((0, 0, 0, 0, -1), (-1, 0, -1, 0, -1)),
    "l": ((0, 0, 0, 0, -1), (0, 0, 0, 0, -1)),
    "m": ((-1, 0, 0, 0, -1), (-1, -1, 0, 0, -1)),
    "n": ((-1, 0, 0, 0, -1), (-1, -1, 0, 0, -1)),
    "o": ((-1, -1, 1, -1, -1), (-1, -1, 1, -1, -1)),
    "p": ((-1, 0, 0, 0, 0), (-1, -1, 1, -1, -1)),
    "q": ((-1, -1, 1, -1, -1), (-1, 0, 0, 0, 0)),
    "r": ((-1, 0, 0, 0, -1), (-1, 1, -1, -1, -1)),
    "s": ((-1, -1, 0, -1, -1), (-1, -1, 0, -1, -1)),
    "t": ((-1, 1, -1, -1, -1), (-1, 1, -1, 1, -1)),
    "u": ((-1, 0, 0, -1, -1), (-1, 0, 0, 0, -1)),
    "v": ((-1, 1, -1, -1, -1), (-1, 1, -1, -1, -1)),
    "w": ((-1, 1, -1, -1, -1), (-1, 1, -1, -1, -1)),
    "x": ((-1, 1, -1, 1, -1), (-1, 1, -1, 1, -1)),
    "y": ((-1, 1, -1, -1, 1), (-1, 1, -1, -1, -1)),
    "z": ((-1, 1, -1, 1, -1), (-1, 1, -1, 1, -1)),
}


def group_letters(letters, side_index):
    groups = {}
    for letter, sides in letters.items():
        side = sides[side_index][:4] # Consider only the first four digits
        if side not in groups:
            groups[side] = []
        groups[side].append(letter)
    return groups

def print_groups(groups):
    for i, (side, letters) in enumerate(groups.items()):
        print(f"Group {i+1}")
        print(" ".join(letters))
        print()

def list_combinations(leftside_groups, rightside_groups):
    left_letters = [letters[0] for _, letters in leftside_groups.items()]
    right_letters = [letters[0] for _, letters in rightside_groups.items()]

    combinations = list(itertools.product(right_letters, left_letters))
    
    for i, (right_letter, left_letter) in enumerate(combinations):
        print(f"{right_letter}{left_letter}", end="")
        if (i + 1) % 15 == 0:
            print()

# Group by rightside
rightside_groups = group_letters(letters, 1)
print("Group by Rightside:")
print("========================================")
print("")
print_groups(rightside_groups)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

# Group by leftside
leftside_groups = group_letters(letters, 0)
print("Group by Leftside:")
print("========================================")
print("")
print_groups(leftside_groups)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Combinations (Rightside + Leftside):")
print("========================================")
list_combinations(leftside_groups, rightside_groups)