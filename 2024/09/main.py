import time
import sys

# Insanely shit solution
class Solution:
    def __init__(self, is_test=False):
        self.is_test = is_test
        self.file_name = "testinput.txt" if is_test else "input.txt"
        self.data = open(self.file_name).read().strip()

    def parse(self):
        db = []
        fid = 0
        f = True
        for l in map(int, self.data):
            if f:
                db.extend([fid]*l)
                fid += 1
            else:
                db.extend(['.']*l)
            f = not f
        return db

    def part1(self):
        db = self.parse()
        for i in range(len(db) - 1, -1, -1):
            if db[i] != '.':
                fi = 0
                while fi < len(db) and db[fi] != '.':
                    fi += 1
                if fi < i:
                    db[fi] = db[i]
                    db[i] = '.'
        ch = 0
        for p, b in enumerate(db):
            if b != '.':
                ch += p * b
        return ch

    def part2(self):
        db = self.parse()
        mfid = max(b for b in db if b != '.')
        for f_id in range(mfid, -1, -1):
            fi_list = [i for i, b in enumerate(db) if b == f_id]
            if not fi_list:
                continue
            fs = len(fi_list)
            fs_start = min(fi_list)
            frs = -1
            frl = 0
            ts = -1
            for i in range(fs_start):
                if db[i] == '.':
                    if frs == -1:
                        frs = i
                    frl += 1
                    if frl == fs:
                        ts = frs
                        break
                else:
                    frs = -1
                    frl = 0
            if ts != -1:
                for idx in fi_list:
                    db[idx] = '.'
                for j in range(fs):
                    db[ts+j] = f_id
        ch = 0
        for p, b in enumerate(db):
            if b != '.':
                ch += p * b
        return ch


def main():
    time_start = time.perf_counter()
    s = Solution(is_test=True)
    print('---Test---')
    print(f"Part 1: {s.part1()}")
    print(f"Part 2: {s.part2()}")
    s = Solution()
    print('---Real---')
    print(f"Part 1: {s.part1()}")
    print(f"Part 2: {s.part2()}")
    print(f"{time.perf_counter()-time_start:.4f}")


main()
