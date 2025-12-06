from mathsolver import MathSolver


solver = MathSolver()


def solve(data, method):
    with open(data, "r") as f:
        data_list = []
        for line in f:
            data_list.append(line)
        solver.prepare_arrays(data_list, method)
        return solver.calculate_sum()


def check(answer, key):
    return "Too small" if answer < key else "Too big" if answer > key else "Solved"


print(check(solve("scripts/day6/toy_input6.txt", 1), 4277556))
print(solve("scripts/day6/input6.txt", 1))
print(check(solve("scripts/day6/toy_input6.txt", 2), 3263827))
print(solve("scripts/day6/input6.txt", 2))
