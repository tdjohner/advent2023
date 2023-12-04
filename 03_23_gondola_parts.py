# Teagan Johner
# Advent of Code 2023
# Day 03
# https://adventofcode.com/2023/day/3
#
# Part ONE:
# The gondola part numbers are hidden in the text file.
#  Any number adjacent to a symbol, including diagonally is a part number.
#  Get the sum of the part numbers
#
# Part TWO:

import os
import re
from aocd import get_data

# The data contains only symbols, numbers, and "."
nonce = '.'
symbol = '[^a-zA-Z0-9\.\n]' 
number = '[0-9]+'

# List of tuples: (x, y, char) for symbol locations
symbol_indexes = []
# List of tuples: (x, y, number, end) for number locations
number_indexes = []
# List of tuples: (number, x, y) A number adjacent to a symbol is a valid part number
part_numbers = set()

os.environ["AOC_SESSION"] = "53616c7465645f5fa0677714e7f313c514ccdfe2bb60568ba7d9aec24ed0f0d5aebbf2e0b1b2bdb42f213a69c29be3d6db90be989c343cf6c8be5e3327e3a2c5"
data = get_data(day=3, year=2023)


# Get the index data for all symbols and numbers
row = 0 # y index 
for line in data.split('\n'):
    [symbol_indexes.append((sym.start(0), row, sym.group(0))) for sym in re.finditer(symbol, line)]             # (x, y, symbol)
    [number_indexes.append((num.start(0), row, num.group(0), num.end(0))) for num in re.finditer(number, line)] # (x, y, number, end)
    row += 1

# Evaluate symbol and number coordinates to determine valid "part numbers"
# For each number see if a symbol is within 1 column and within 1 row:
for n in number_indexes:
    x_number_start = n[0]
    x_number_end = n[3]
    y_number = n[1]
    for s in symbol_indexes:
        x_symbol = s[0]
        y_symbol = s[1]
        # symbol is within 1 row of number
        if y_number - 1 <= y_symbol <= y_number + 1:
            # symbol is within 1 column of number, on either side
            if x_number_start - 1 <= x_symbol <= x_number_end:
                # save number and location, duplicates not allowed
                part_numbers.add((n[2], n[0], n[1])) # (number, x, y)

total = sum([int(p[0]) for p in part_numbers])
print(total)







