from SafeSolver import SafeSolver

data = []
with open("scripts/day1/input1.txt", "r") as f:
    while True:
        line = f.readline().strip()
        if line:
            data.append(line)
        else:
            break

method = 2
solver = SafeSolver(method)
answer = solver.solver(data)
print(answer)
