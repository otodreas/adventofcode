import re
import numpy as np


class MathSolver:
    def __init__(self):
        pass

    def prepare_arrays(self, data_list, method):
        self.operations = re.split(r"\s+", data_list[-1].strip())
        if method == 1:
            digits_list = [re.split(r"\s+", line.strip()) for line in data_list[:-1]]
            self.numbers = np.array(digits_list, dtype=np.int16).T
        else:
            digits_list = [(list(line.strip("\n"))) for line in data_list[:-1]]
            digits_arr = np.array(digits_list, dtype=np.str_).T
            numbers_list, numbers_row = [], []
            for digits in digits_arr:
                if np.sum(digits == " ") < len(digits):
                    numbers_row.append(np.int16("".join(digits).strip()))
                else:
                    numbers_list.append(numbers_row)
                    numbers_row = []
            numbers_list.append(numbers_row)
            self.numbers = numbers_list

    def calculate_sum(self):
        sum = 0
        for i, n in enumerate(self.numbers):
            sum += np.sum(n) if self.operations[i] == "+" else np.prod(n)
        return sum
