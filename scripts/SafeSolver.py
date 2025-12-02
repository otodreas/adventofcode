import math

class SafeSolver:
    def __init__(self, method, n_vals = 100):
        self.method = method
        self.rng = list(range(n_vals))

    def position_looper(self, p, step):
        clicks = p + step  # Determine how many "clicks" away from the starting position you end up
        cycles = math.floor(clicks/len(self.rng))  # Determine how many cycles through the range have been completed
        p_new = clicks - cycles * len(self.rng)  # Adjust the position by "resetting" the position at every cycle

        zeros_passed = abs(cycles) #if p != 0 else abs(cycles) - 1
        # if step <= 0 and p_new == 0 and zeros_passed > 1:
        # print(f"{p} + {step} = {p_new}, {cycles} {zeros_passed}")

        return [p_new, zeros_passed]

    def solver(self, data, start_pos = 50):
        self.data = data
        self.start_pos = start_pos
        position = self.start_pos
        answer = 0
        step_previous = None

        for d in data:
            increment = int(d[1:])
            direction = 1 if d[0] == "R" else -1
            position, zeros_passed = self.position_looper(position, increment * direction)
            if self.method == 1:
                if position == 0:
                    answer += 1
            else:
                answer += zeros_passed

        return answer