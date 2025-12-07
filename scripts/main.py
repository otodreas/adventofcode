from day6 import mathsolver
from day7 import beamsplitter

ms = mathsolver.MathSolver()
bs = beamsplitter.BeamSplitter()


def check(answer, key):
    return "Too small" if answer < key else "Too big" if answer > key else "Solved"


def file_list_reader(fp):
    with open(fp, "r") as f:
        data_list = []
        for line in f:
            data_list.append(line)
        return data_list
    

def solve_math(data, method, key=None):
    data_list = file_list_reader(data)
    ms.prepare_arrays(data_list, method)
    if key:
        return check(ms.calculate_sum(), key)
    else:
        return ms.calculate_sum()


def solve_beam(data, method=1, key=None):
    data_list = file_list_reader(data)
    return bs.find_splits(data_list)



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

print(solve_beam(files[0], 1, keys[0]))
print(solve_beam(files[1], 1))
print(solve_beam(files[0], 2, keys[1]))
