# Teagan Johner
# Advent of Code 2023
# Day 01
# https://adventofcode.com/2023/day/1
#
# Part ONE:
# A set number of marbles, each of 3 colors go into the bag.
# Data is provided detailing a number of revealed marbles. Find
# the sum of IDs of games where the number cubes revealed does
# not surpass the maximum number for those cubes' color.
#
# Part TWO:
# The minimum number of cubes required for each time that
#  color of cubes was revealed to be possible, multiplied together
# "Power of Cubes" minRed * minBlue * minGreen

import os
import re
from aocd import get_data

os.environ["AOC_SESSION"] = ""
data = get_data(day=2, year=2023)
games = data.split('\n')


color_maximums = {"red": 12, "green": 13, "blue": 14}   # The max number for each color that can be revealed during a game
color_minimums = {"red": 0, "green": 0, "blue": 0}      # The least number of cubes possible for each game to be valid
invalid_games = set()   # Any game that has a draw that has a color that exceeds the color maximum
all_games = set()       # All game IDs
powers_of_cubes = []    # Lowest number of each color of cubes revealed in a draw, per game

for game in games:
    
    # We want to evaluate the minimums for each game so init here
    color_minimums = {"red": 0, "green": 0, "blue": 0}
    
    # Parsing out the data (we are taking some extreme liberties because we know the format)
    game_header = re.search('^Game \d+ ?\:', game) 
    game = game.replace(game_header.group(0), "")
    game_id = int(game_header.group(0).split()[1].replace(":",""))
    all_games.add(game_id)
    
    # A round is a set of draws revealed from the bag
    for round in game.split(";"):
        
        # A 'draw' is number of cubes and their color, revealed during a round
        for draw in round.split(","):
            color_of_cubes = re.search('[a-z]+', draw).group(0)
            number_of_cubes = int(re.search('[0-9]+' , draw).group(0))

            # Store the highest value for this color during this game            
            color_minimums[color_of_cubes] = max(color_minimums[color_of_cubes], number_of_cubes)

            if number_of_cubes > color_maximums[color_of_cubes]:
                invalid_games.add(game_id)
                   
    # Store "power of cubes" for this game
    powers_of_cubes.append(color_minimums["red"] * color_minimums["blue"] * color_minimums["green"])

print(sum(all_games - invalid_games))
print(sum(powers_of_cubes))