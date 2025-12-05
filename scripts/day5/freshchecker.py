import numpy as np


class FreshChecker:
    def __init__(self):
        pass

    def get_ranges(self, data):
        ranges = data
        range_indices_array = np.zeros((len(data), 2), dtype=np.int64)
        for i, r in enumerate(ranges):
            nums = r.split("-")
            range_indices_array[i] = np.array([nums[0], int(nums[1]) + 1])

        range_indices_array_sorted = np.sort(range_indices_array, 0)
        ranges = []
        for i, r in enumerate(range_indices_array_sorted):
            ranges.append(range(r[0], r[1]))

        self.ranges = ranges

    def check_fresh(self, id):
        for r in self.ranges:
            if id in r:
                return True
        return False

    def count_fresh_ids(self):
        NOLs = [self.ranges[0]]  # Non-overlapping lengths
        for r in self.ranges[1:]:
            r_p = NOLs[-1]
            if (
                r_p[0] < r[-1] + 1
                and r_p[-1] + 1 > r[0]
                or r[0] < r_p[-1] + 1
                and r[-1] + 1 > r_p[0]
            ):
                NOLs[-1] = range(min(r_p[0], r[0]), max(r_p[-1] + 1, r[-1] + 1))
            else:
                NOLs.append(r)

        fresh_ids = 0
        for NOL in NOLs:
            fresh_ids += len(NOL)

        return fresh_ids
