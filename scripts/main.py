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

solver = SafeSolver(2)
answer = solver.solver(data)#[:50])
print(answer)

# print(SafeSolver(2).solver(data))