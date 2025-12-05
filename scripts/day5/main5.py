import linecache
from freshchecker import FreshChecker


def solve(fp, method):
    fc = FreshChecker()
    fresh_sum = 0
    with open(fp, "r") as file:
        i = 0
        ranges_raw = []
        while True:
            i += 1
            range_raw = file.readline().strip()
            if range_raw:
                ranges_raw.append(range_raw)
            else:
                fc.get_ranges(ranges_raw)
                break
        
        if method == 1:
            while True:
                i += 1
                id = linecache.getline(fp, i)
                if id:
                    fresh_sum += fc.check_fresh(int(id))
                else:
                    break

            return fresh_sum
        
        else:
            n_fresh_ids = fc.count_fresh_ids()

            return n_fresh_ids

def check(answer, key):
    if answer < key:
        return "Too small"
    elif answer > key:
        return "Too large"
    else:
        return "Solved"


print(check(solve("scripts/day5/toy_input5.txt", 1), 3))
# print(solve("scripts/day5/input5.txt", 1))
print(check(solve("scripts/day5/toy_input5.txt", 2), 14))
# print(solve("scripts/day5/input5.txt", 2))
x = range(1, 11)
y = range(5, 16)
print(range(max(x[0], y[0]), min(x[-1], y[-1])+1))
# print(len([x, y]))