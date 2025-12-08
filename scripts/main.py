from day6 import mathsolver
from day7 import beamsplitter

ms = mathsolver.MathSolver()
bs = beamsplitter.BeamSplitter()


def check(answer, key=None):
    if key:
        return "Too small" if answer < key else "Too big" if answer > key else "Solved"
    else:
        return answer


def file_list_reader(fp):
    with open(fp, "r") as f:
        data_list = []
        for line in f:
            data_list.append(line)
        return data_list


def solve_math(data, method, key=None):
    data_list = file_list_reader(data)
    ms.prepare_arrays(data_list, method)
    return check(ms.calculate_sum(), key)


def solve_beam(data, method=1, key=None):
    data_list = file_list_reader(data)
    return check(bs.count_splits(data_list), key) if method == 1 else check(bs.count_paths(data_list), key)


# # Solve day 6 problems
# files = ["scripts/day6/toy_input6.txt", "scripts/day6/input6.txt"]
# keys = [4277556, 3263827]

# print(solve_math(files[0], 1, keys[0]))
# print(solve_math(files[1], 1))
# print(solve_math(files[0], 2, keys[1]))
# print(solve_math(files[1], 2))

# Solve day 7 problems
files = ["scripts/day7/toy_input7.txt", "scripts/day7/input7.txt"]
keys = [21, 40]

# print(solve_beam(files[0], 1, keys[0]))
# print(solve_beam(files[1], 1))
print(solve_beam(files[0], 2, keys[1]))
# print(solve_beam(files[1], 2))