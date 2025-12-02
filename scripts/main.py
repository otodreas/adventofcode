from SafeSolver import SafeSolver
i = 0
data = []
with open("scripts/input.txt", "r") as f:
    while True:
    # while i<5:
        # i += 1
        line = f.readline().strip()
        if line:
            data.append(line)
        else:
            break

solver = SafeSolver(1)
answer = solver.solver(data)
print(answer)
# print(SafeSolver.position_looper(self=solver, p=1, step_prev=0, step=-1)[2])

# 0 -> + : the starting 0 is NOT counted
# 0 -> - : the starting 0 IS counted
# + -> 0 : the ending 0 IS counted
# - -> 0 : the ending 0 is NOT counted