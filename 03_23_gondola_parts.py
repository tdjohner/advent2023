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
# Any "*" symbol that is adjacent to exactly two numbers is a gear.
#  the "gear ratio" is the multiple of those two numbers. Get the 
#  sum of the gear ratios.

import os
import re
from aocd import get_data

# Regular expressions to parse out the numbers and symbols
symbol = '[^a-zA-Z0-9\.\n]' 
number = '[0-9]+'

# List of tuples: (x, y, char) for symbol locations
symbol_indexes = []
# List of tuples: (x, y, number, end) for number locations
number_indexes = []
# List of tuples: (number, x, y) A number adjacent to a symbol is a valid part number
part_numbers = set()
# Gear ratios: (number object, symbol object)
potential_gear_ratios = set()
# Gear ratios: x = number1 * number2
gear_ratios = []
# Need to track gear objects to avoid duplicating gear ratios
verified_gears = set()

os.environ["AOC_SESSION"] = ""
data = get_data(day=3, year=2023)


# Get the index data for all symbols and numbers
row = 0 # y index 
for line in data.split('\n'):
    [symbol_indexes.append((sym.start(0), row, sym.group(0))) for sym in re.finditer(symbol, line)]             # (x, y, symbol)
    [number_indexes.append((num.start(0), row, num.group(0), num.end(0))) for num in re.finditer(number, line)] # (x, y, number, end)
    row += 1

# Evaluate symbol and number coordinates to determine valid "part numbers"
for s in symbol_indexes:
    x_symbol = s[0]
    y_symbol = s[1]
    symbol_value = s[2]
    for n in number_indexes:
        x_number_start = n[0]
        x_number_end = n[3]
        y_number = n[1]
        
        # symbol is within 1 row of number
        if y_number - 1 <= y_symbol <= y_number + 1:
            # symbol is within 1 column of number, on either side
            if x_number_start - 1 <= x_symbol <= x_number_end:
                # save number and location, duplicates not allowed
                part_numbers.add((n[2], n[0], n[1])) # (number, x, y)
                
                # only "*" characters can be gears.
                if symbol_value == "*":
                    # Add to the set for later evaluation
                    potential_gear_ratios.add((n, s))                
                        
# recall gear ratios: (number object, symbol object) : ((x, y, number, end), (x, y, symbol))        
for g1 in potential_gear_ratios:
    if (g1[1] not in verified_gears):
        for g2 in potential_gear_ratios:
            if g1 != g2 and g1[1] == g2[1]:
                gear_ratios.append(int(g1[0][2]) * int(g2[0][2]))
                verified_gears.add(g1[1]) # add the gear to the known gear ratios

total = sum([int(p[0]) for p in part_numbers])
gear_ratios_total = sum(gear_ratios)
print("Part number:", total)
print("Gear ratios sum:", gear_ratios_total)






