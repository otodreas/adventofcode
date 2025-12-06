from day6 import mathsolver

math_solver = mathsolver.MathSolver()


def check(answer, key):
    return "Too small" if answer < key else "Too big" if answer > key else "Solved"


def solve_math(data, method, key=None):
    with open(data, "r") as f:
        data_list = []
        for line in f:
            data_list.append(line)
        math_solver.prepare_arrays(data_list, method)
        if key:
            return check(math_solver.calculate_sum(), key)
        else:
            return math_solver.calculate_sum()


print(solve_math("scripts/day6/toy_input6.txt", 1, 4277556))
print(solve_math("scripts/day6/input6.txt", 1))
print(solve_math("scripts/day6/toy_input6.txt", 2, 3263827))
print(solve_math("scripts/day6/input6.txt", 2))
