import math


class idParser:
    def __init__(self):
        pass

    def make_data_list(self, txt_data):
        self.txt_data = txt_data
        txt_data_list = txt_data.split(sep=",")

        values = []
        for d in txt_data_list:
            pair = d.split(sep="-")
            for i in [0, 1]:
                pair[i] = int(pair[i])
            # Ensure that the entire range is accounted for, including the last number
            values.append(range(pair[0], pair[1] + 1))

        return values

    def parse1(self, values, tb=False):
        """
        This method calculates the sum of invalid id's. Invalid id's are
        defined as id's made up EXACTLY two identical sequences.
            For example: 1212 (12 twice), 44 (4 twice)
        """
        self.values = values
        self.tb = tb
        sum_invalid_ids = 0

        for pair in values:
            # Since pair is a range, get all values in range in a list
            ids = list(pair)
            for id in ids:
                # Prepare id for slicing by converting to string
                id = str(id)
                # Only test if id has an even number of digits. If not, it must be valid
                if len(id) % 2 == 0:
                    midpoint = int(len(id) / 2)
                    front = id[:midpoint]
                    back = id[midpoint:]
                    if front == back:
                        sum_invalid_ids += int(id)
                        if tb:
                            print(int(id))

        return sum_invalid_ids

    def parse2(self, values, tb=False):
        """
        This method calculates the sum of invalid id's. Invalid id's are
        defined as id's made up two OR MORE identical sequences
            For example: 1212, 44, 999, 567567567.
        """
        self.values = values
        self.tb = tb
        sum_invalid_ids = 0

        for pair in values:
            ids = list(pair)
            for id in ids:
                id = str(id)
                # Loop through all slice sizes up to 1/2 the number of digits in the id in integers
                for i in range(1, math.floor(len(id) / 2) + 1):
                    # Check that the number of digits in the id is evenly divisible by the slice size
                    if len(id) % i == 0:
                        slices = []
                        # Loop through each slice position for a given slice size
                        for j in range(int(len(id) / i)):
                            # Get each even slice and append to the list slices
                            slices.append(id[j * i : (j + 1) * i])
                        if len(set(slices)) == 1:
                            sum_invalid_ids += int(id)
                            if tb:
                                print(int(id))
                            # Break loop to prevent double-counting invalid id's that may be invalid in more ways than one
                            break

        return sum_invalid_ids
