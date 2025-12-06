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


def print_solutions(function, files, keys):
    print(function(files[0], 1, keys[0]))
    print(function(files[1], 1))
    print(function(files[0], 2, keys[1]))
    print(function(files[1], 2))


# Solve day 6 problems
print_solutions(
    solve_math,
    ["scripts/day6/toy_input6.txt", "scripts/day6/input6.txt"],
    [4277556, 3263827],
)
