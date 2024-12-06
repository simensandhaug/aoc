from collections import defaultdict, deque
import numpy as np
import re
import itertools

grid = open("input.txt", "r").read().strip().split("\n")


rows, cols = len(grid), len(grid[0])
part1 = 0
part2 = 0

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '^':
            start_row, start_col = row, col

for obs_row in range(rows):
    for obs_col in range(cols):
        current_row, current_col = start_row, start_col
        direction = 0
        visited_states = set()
        unique_positions = set()

        while True:
            if (current_row, current_col, direction) in visited_states:
                part2 += 1
                break
            visited_states.add((current_row, current_col, direction))
            unique_positions.add((current_row, current_col))

            delta_row, delta_col = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
            next_row, next_col = current_row + delta_row, current_col + delta_col

            if not (0 <= next_row < rows and 0 <= next_col < cols):
                if grid[obs_row][obs_col] == '#':
                    part1 = len(unique_positions)
                break
            if grid[next_row][next_col] == '#' or (next_row, next_col) == (obs_row, obs_col):
                direction = (direction + 1) % 4
            else:
                current_row, current_col = next_row, next_col

print(part1)
print(part2)
