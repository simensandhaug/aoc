from collections import defaultdict, deque
import numpy as np
import re
import itertools

lines = open("input.txt", "r").read().strip().split("\n")


def p1():
    return sum(int(x) * int(y) for line in lines for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line))



def p2():
    total = 0
    enabled = True 
    tokens = re.split(r"(\bdo\(\)|\bdon't\(\)|mul\(\d{1,3},\d{1,3}\))", " ".join(lines))
    for token in tokens:
        enabled = True if re.match(r"do\(\)", token) else False if re.match(r"don't\(\)", token) else enabled
        if re.match(r"mul\((\d{1,3}),(\d{1,3})\)", token) and enabled:
            x, y = map(int, re.findall(r"\d{1,3}", token))
            total += x*y
    return total


print(f"Part 1: {p1()}")
print(f"Part 2: {p2()}")

