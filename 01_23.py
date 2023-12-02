# Teagan Johner
# Advent of Code 2023
# Day 01
# https://adventofcode.com/2023/day/1
#
# Each line has a hidden number. Get the sum of all the hidden numbers.
# The hidden number is the first and last numberic character on each line.
# Lines with a single numeric are multiples of 11 i.e. tre7chet -> 77

import os
from aocd import get_data

os.environ["AOC_SESSION"] = ""
data = get_data(day=1, year=2023)
lines = data.split()


total = 0               # Store the sum of each line's hidden number
for line in lines:
    digits = [d for d in line if d.isdigit()]   # Go over the line and get all the numeric chars
    total += int(digits[0] + digits[-1])        # Add secret number to total, do not store we only want the sum

print(total)
