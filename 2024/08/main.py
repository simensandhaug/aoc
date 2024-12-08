import math
import itertools
import time
from collections import defaultdict

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        
    def part1(self):
        ants, w, h = self.parse_map(self.data)
        return self.find_antinodes(ants, w, h)

    def part2(self):
        ants, w, h = self.parse_map(self.data)
        return self.find_antinodes(ants, w, h, part2=True)

    def parse_map(self, map_data):
        ants = defaultdict(list)
        rows = map_data.strip().split("\n")
        for y, row in enumerate(rows):
            for x, char in enumerate(row):
                if char != '.':
                    ants[char].append((x, y))
        return ants, len(rows[0]), len(rows)

    def find_antinodes(self, ants, w, h, part2=False):
        anodes = set()

        for f, p in ants.items():
            for p1, p2 in itertools.combinations(p, 2):
                x1, y1 = p1
                x2, y2 = p2
                dx = x2 - x1
                dy = y2 - y1
                
                if not part2:
                    ax1, ay1 = x1 - dx, y1 - dy
                    if 0 <= ax1 < w and 0 <= ay1 < h:
                        anodes.add((ax1, ay1))

                    ax2, ay2 = x2 + dx, y2 + dy
                    if 0 <= ax2 < w and 0 <= ay2 < h:
                        anodes.add((ax2, ay2))
                else:
                    g = abs(math.gcd(dx, dy))
                    step_x = dx // g
                    step_y = dy // g

                    px, py = x1, y1
                    while 0 <= px < w and 0 <= py < h:
                        anodes.add((px, py))
                        px += step_x
                        py += step_y

                    px, py = x1 - step_x, y1 - step_y
                    while 0 <= px < w and 0 <= py < h:
                        anodes.add((px, py))
                        px -= step_x
                        py -= step_y

        return len(anodes)

def main():
    start = time.perf_counter()
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

if __name__ == "__main__":
    main()
