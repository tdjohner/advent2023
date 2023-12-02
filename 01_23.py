# Teagan Johner
# Advent of Code 2023
# Day 01
# https://adventofcode.com/2023/day/1
#
# Part ONE:
# Each line has a hidden number. Get the sum of all the hidden numbers.
# The hidden number is the first and last numberic character on each line.
# Lines with a single numeric are multiples of 11 i.e. tre7chet -> 77
#
# PART TWO:
# The lines may also have numbers spelled out.

import os
from aocd import get_data

os.environ["AOC_SESSION"] = ""
data = get_data(day=1, year=2023)
lines = data.split()

# Adding the "1" : "1" pairs allows us to do all comparisons in 1 place.
calibration_digits = {
    "1": "1", "one": "1",
    "2": "2", "two": "2",
    "3": "3", "three": "3",
    "4": "4", "four": "4",
    "5": "5", "five": "5",
    "6": "6", "six": "6",
    "7": "7", "seven": "7",
    "8": "8", "eight": "8",
    "9": "9", "nine": "9" }

total = 0
for line in lines:
    
    # We will store any occurences in a dictionary { index: digit value}
    digits = {}
    for cd in calibration_digits:                            # Scan for all digit keys
        if cd in line:
            digits[line.index(cd)] = calibration_digits[cd]  # Store first occurence in a dictionary
            digits[line.rindex(cd)] = calibration_digits[cd] # We only care about the first and last occurences
            
    total += int(digits[min(digits)] + digits[max(digits)])  # Concat occurences at highest/lowest indexes in digits{}