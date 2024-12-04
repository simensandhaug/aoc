from collections import defaultdict, deque
import numpy as np
import re
import itertools

lines = open("input.txt", "r").read().strip().split("\n")

grid = [list(line) for line in lines]
def p1():
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    word = "XMAS"
    count = 0
    
    def check_word(r, c, dr, dc):
        for i in range(len(word)):
            nr, nc = r + dr * i, c + dc * i
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_word(r, c, dr, dc):
                    count += 1
    
    return count


def p2():
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_xmas_cross(r, c):
        if (
            r - 1 >= 0 and r + 1 < rows and c - 1 >= 0 and c + 1 < cols and
            (
                (grid[r - 1][c - 1] == "M" and grid[r + 1][c + 1] == "S" or grid[r - 1][c - 1] == "S" and grid[r + 1][c + 1] == "M") and
                (grid[r - 1][c + 1] == "M" and grid[r + 1][c - 1] == "S" or grid[r - 1][c + 1] == "S" and grid[r + 1][c - 1] == "M")
            )
        ):
            return True
        return False

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "A" and is_xmas_cross(r, c):
                count += 1

    return count

print(f"Part 1: {p1()}")
print(f"Part 2: {p2()}")

