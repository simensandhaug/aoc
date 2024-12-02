from collections import defaultdict, deque
import numpy as np
import re
import itertools

lines = open("input.txt", "r").read().strip().split("\n")

def check_safe(nums):
    if len(nums) < 2:
        return False
        
    inc_dec_constraint = False
    if all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)):
        inc_dec_constraint = True
    elif all(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
        inc_dec_constraint = True
    
    adj_constraint = True
    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i + 1])
        if diff < 1 or diff > 3:
            adj_constraint = False
            break
        
    return inc_dec_constraint and adj_constraint

def p1():
    num_safe = 0
    for report in lines:
        nums = [int(x) for x in report.split(" ")]
        
        if check_safe(nums):
            num_safe += 1
            
    return num_safe


def p2():
    num_safe = 0
    for report in lines:
        nums = [int(x) for x in report.split(" ")]
        
        if check_safe(nums):
            num_safe += 1
            continue
            
        for i in range(len(nums)):
            test_nums = nums[:i] + nums[i+1:]
            if check_safe(test_nums):
                num_safe += 1
                break
                
    return num_safe

print(f"Part 1: {p1()}")
print(f"Part 2: {p2()}")

