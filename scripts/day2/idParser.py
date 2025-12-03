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
            values.append(range(pair[0], pair[1] + 1))

        return values

    def parse1(self, values, tb=False):
        self.values = values
        self.tb = tb
        sum_invalid_ids = 0

        for pair in values:
            ids = list(pair)
            for id in ids:
                id = str(id)
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
        self.values = values
        self.tb = tb
        sum_invalid_ids = 0

        for pair in values:
            ids = list(pair)
            for id in ids:
                id = str(id)
                for i in range(1, math.floor(len(id) / 2) + 1):
                    if len(id) % i == 0:
                        slices = []
                        for j in range(int(len(id) / i)):
                            slices.append(id[j * i : (j + 1) * i])
                        if len(set(slices)) == 1:
                            sum_invalid_ids += int(id)
                            if tb:
                                print(int(id))
                            break

        return sum_invalid_ids
