class Joltage:
    def __init__(self):
        pass

    def maximize_joltage(self, bank, n_digits):
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
