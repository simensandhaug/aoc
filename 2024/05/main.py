from collections import defaultdict, deque

with open("input.txt", "r") as file:
    lines = file.read().strip().split("\n")

rules_lines = []
updates_lines = []
in_rules_section = True

for line in lines:
    if line.strip() == "":
        in_rules_section = False
    elif in_rules_section:
        rules_lines.append(line.strip())
    else:
        updates_lines.append(line.strip())

rules = [tuple(map(int, rule.split("|"))) for rule in rules_lines]
updates = [list(map(int, update.split(","))) for update in updates_lines]

def is_ordered(update, rules):
    p_pos = {p: i for i, p in enumerate(update)}
    
    for rule in rules:
        pa1, pa2 = rule
        if pa1 in p_pos and pa2 in p_pos:
            if p_pos[pa1] > p_pos[pa2]:
                return False
    return True


def topological_sort(pages, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for pa1, pa2 in rules:
        if pa1 in pages and pa2 in pages:
            graph[pa1].append(pa2)
            in_degree[pa2] += 1
            if pa1 not in in_degree:
                in_degree[pa1] = 0
    
    q = deque([p for p in pages if in_degree[p] == 0])
    sorted_pages = []
    
    while q:
        p = q.popleft()
        sorted_pages.append(p)
        
        for n in graph[p]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                q.append(n)
    
    return sorted_pages

def p1():
    valid = []
    for update in updates:
        if is_ordered(update, rules):
            valid.append(update[len(update) // 2])
    return sum(valid)

def p2():
    incorrect = []
    for update in updates:
        if not is_ordered(update, rules):
            incorrect.append(topological_sort(update, rules))
    middle_pages = [u[len(u) // 2] for u in incorrect]
    return sum(middle_pages)

print(f"Part 1: {p1()}")
print(f"Part 2: {p2()}")
