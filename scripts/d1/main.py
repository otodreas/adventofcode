from SafeSolver import SafeSolver

# Import data
data = []
with open("scripts/d1/input.txt", "r") as f:
    while True:
        line = f.readline().strip()
        if line:
            data.append(line)
        else:
            break

# Run solver
solver = SafeSolver()
answer = solver.solver(data)
print(answer)