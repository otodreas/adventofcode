# Import libraries
import math

# Define class
class SafeSolver:
    def __init__(self, n_vals = 100):
        self.rng = list(range(n_vals))

    def position_looper(self, p, step):
        # Determine how many "clicks" away from the starting position you end up
        clicks = p + step
        # Determine how many cycles through the range have been completed
        cycles = math.floor(clicks/len(self.rng))
        # Adjust the position by "resetting" the position at every cycle
        p_new = clicks + -cycles * len(self.rng)

        return p_new

    def solver(self, data, start_pos = 50):
        self.data = data
        self.start_pos = start_pos
        position = self.start_pos
        answer = 0

        for d in data:
            # Get increment from row in data
            increment = int(d[1:])
            # Get sign of increment
            direction = 1 if d[0] is "R" else -1
            # Update the position using position_looper
            position = self.position_looper(position, increment * direction)
            # Update answer if position is 0
            if position == 0:
                answer += 1

        return(answer)