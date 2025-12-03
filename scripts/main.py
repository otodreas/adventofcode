from SafeSolver import SafeSolver
i = 0
data = []
with open("scripts/input.txt", "r") as f:
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