import math

class SafeSolver:
    def __init__(self, n_vals = 100):
        self.rng = list(range(n_vals))

    def position_looper(self, p, step):
        clicks = p + step  # Determine how many "clicks" away from the starting position you end up
        cycles = math.floor(clicks/len(self.rng))  # Determine how many cycles through the range have been completed
        p_new = clicks - cycles * len(self.rng)  # Adjust the position by "resetting" the position at every cycle
        return p_new

    def solver(self, data, start_pos = 50):
        self.data = data
        self.start_pos = start_pos
        position = self.start_pos
        answer = 0

        for d in data:
            increment = int(d[1:])
            direction = 1 if d[0] is "R" else -1
            position = self.position_looper(position, increment * direction)
            if position == 0:
                answer += 1

        return(answer)