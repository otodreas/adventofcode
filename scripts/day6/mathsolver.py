import re
import numpy as np


class MathSolver:
    def __init__(self):
        pass

    def prepare_arrays(self, data_list, method):
        # Assign operation symbols as attribute
        self.operations = re.split(r"\s+", data_list[-1].strip())
        if method == 2:
            # Get individual characters including spaces from the number rows
            digits_list = [(list(line.strip("\n"))) for line in data_list[:-1]]
            # Transform data so that vertically conserved spaces are rows in an array
            digits_arr = np.array(digits_list, dtype=np.str_).T
            # Loop through rows of numerical data
            numbers_list = []
            numbers_row = []
            for digits in digits_arr:
                if np.sum(digits == " ") < len(digits):
                    # Add numbers to a "row" in the list of numbers
                    numbers_row.append(int("".join(digits).strip()))
                else:
                    # Add the "row" of numbers to the list of numbers and reassing the "row" list to an empty list
                    numbers_list.append(numbers_row)
                    numbers_row = []
            # Append the final "row" of numbers to the list of numbers and assign as attribute
            numbers_list.append(numbers_row)
            # Since each "row" of numbers can have different lengths, do not convert to numpy array
            self.numbers = numbers_list

        else:
            # Get numbers in each row of text
            digits_list = [re.split(r"\s+", line.strip()) for line in data_list[:-1]]
            # Create array, transform so that operations are performed on rows, assign as attribute
            self.numbers = np.array(digits_list, dtype=np.int16).T

    def calculate_sum(self):
        sum = 0
        for i, n in enumerate(self.numbers):
            sum += np.sum(n) if self.operations[i] == "+" else np.prod(n)
        return sum
