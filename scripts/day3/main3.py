from Joltage import Joltage


def solve(data, n_digits):
    j = Joltage()
    max_joltage_sum = 0
    with open(data, "r") as f:
        for line in f:
            max_joltage_sum += j.maximize_joltage(line.strip(), n_digits)
    return max_joltage_sum


def test(answer):
    if answer > 0:
        print("Too big")
    elif answer < 0:
        print("Too small")
    else:
        print("Solved")


key1 = 357
correct1 = 17554
key2 = 3121910778619
correct2 = 175053592950232

# solve toy 1
test(solve("scripts/day3/toy_input3.txt", 2) - key1)

# solve part 1
test(solve("scripts/day3/input3.txt", 2) - correct1)

# solve toy 2
test(solve("scripts/day3/toy_input3.txt", 12) - key2)

# solve part 2
test(solve("scripts/day3/input3.txt", 12) - correct2)
