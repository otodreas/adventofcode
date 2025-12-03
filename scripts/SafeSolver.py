import math

class SafeSolver:
    def __init__(self, method, n_vals = 100):
        self.method = method
        self.rng = list(range(n_vals))

    def position_looper(self, p, increment, direction):
        clicks = p + increment * direction  # Determine how many "clicks" away from the starting position you end up
        cycles = self.__cycle_helper(clicks, self.rng)  # Determine how many cycles through the range have been completed
        p_new = clicks - cycles * len(self.rng)  # Adjust the position by "resetting" the position at every cycle

        # Count number of zeros passed, ruling out any instance of landing on zero
        if direction > 0:
            zeros_passed = abs(self.__cycle_helper(clicks - 1, self.rng))
        else:
            if p != 0:
                zeros_passed = abs(self.__cycle_helper(clicks, self.rng))
            else:
                zeros_passed = abs(self.__cycle_helper(clicks, self.rng)) - 1

        return [p_new, zeros_passed]

    def solver(self, data, start_pos = 50):
        self.data = data
        self.start_pos = start_pos
        position = self.start_pos
        answer = 0

        for d in data:
            increment = int(d[1:])
            direction = 1 if d[0] == "R" else -1
            position, zeros_passed = self.position_looper(position, increment, direction)
            if position == 0:
                    answer += 1
            if self.method == 2:
                answer += zeros_passed

        return answer
    
    def __cycle_helper(self, clicks, rng):
        return math.floor(clicks/len(rng))