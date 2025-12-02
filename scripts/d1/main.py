from SafeSolver import SafeSolver

data = []
with open("scripts/d1/input.txt", "r") as f:
    while True:
        line = f.readline().strip()
        if line:
            data.append(line)
        else:
            break

solver = SafeSolver()
answer = solver.solver(data)
print(answer)