from collections import defaultdict, deque
import numpy as np
import re
import itertools
from functools import lru_cache

lines = open("input.txt", "r").read().strip().split("\n")


def evaluate(ns, t, concat=False):
    r = {ns[0]}
    for n in ns[1:]:
        new_r = set()
        for r in r:
            new_r.add(r + n)
            new_r.add(r * n)
            if concat:
                new_r.add(int(str(r) + str(n)))
        r = new_r
    return t in r


def p1():
    ans = 0
    for line in lines:
        t, *ns = map(int, re.split(r": | ", line))
        if evaluate(ns, t, concat=False):
            ans += t
    return ans


def p2():
    ans = 0
    for line in lines:
        t, *ns = map(int, re.split(r": | ", line))
        if evaluate(ns, t, concat=True):
            ans += t
    return ans


print(f"Part 1: {p1()}")
print(f"Part 2: {p2()}")
