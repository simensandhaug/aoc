from collections import Counter

lines = open("input.txt", "r").read().strip().split("\n")

L = []
R = []
RC = Counter()
for line in lines:
    l, r = line.split()
    l, r = int(l), int(r)
    L.append(l)
    R.append(r)
    RC[r] += 1

L = sorted(L)
R = sorted(R)

print(sum(abs(l - r) for l, r in zip(L, R)))
print(sum(l * RC.get(l, 0) for l in L))

