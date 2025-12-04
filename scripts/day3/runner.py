def maximize_joltage(bank, n_digits):
    max_joltage = []
    batteries = list(map(int, list(bank)))
    head = 0
    tail = len(bank) - n_digits + 1
    for _ in range(n_digits):
        b_index = batteries[head:tail].index(max(batteries[head:tail]))
        max_joltage.append(str(batteries[head + b_index]))
        head += b_index + 1
        tail += 1
    return int("".join(max_joltage))


def solve(data, n_digits):
    max_joltage_sum = 0
    with open(data, "r") as f:
        for line in f:
            max_joltage_sum += maximize_joltage(line.strip(), n_digits)
    return max_joltage_sum


print(solve("scripts/day3/input3.txt", 12) - 175053592950232)
