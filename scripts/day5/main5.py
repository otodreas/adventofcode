import linecache
from freshchecker import FreshChecker


def solve(fp, method):
    fc = FreshChecker()
    with open(fp, "r") as file:
        # Get ranges from data file
        ranges_raw = []
        i = 0
        while True:
            i += 1
            range_raw = file.readline().strip()
            if range_raw:
                ranges_raw.append(range_raw)
            else:
                fc.get_ranges(ranges_raw)
                break

        # Count how many id's below the ranges are contained in the ranges
        if method == 1:
            fresh_sum = 0
            while True:
                i += 1
                id = linecache.getline(fp, i)
                if id:
                    fresh_sum += fc.check_fresh(int(id))
                else:
                    break

            return fresh_sum

        # Count how many id's are in the ranges
        else:
            return fc.count_fresh_ids()


def check(answer, key):
    return (
        "Too small" if answer < key else
        "Too large" if answer > key else
        "Solved"
    )


print("Toy data:", check(solve("scripts/day5/toy_input5.txt", 1), 3))
print("Real data:", solve("scripts/day5/input5.txt", 1))
print("Toy data:", check(solve("scripts/day5/toy_input5.txt", 2), 14))
print("Real data:", solve("scripts/day5/input5.txt", 2))
