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
        xranges = [self.ranges[0]]
        for r in self.ranges[1:]:
            r_p = xranges[-1]
            if (r_p[0] < r[-1] + 1 and r[0] < r_p[-1] + 1):
                xranges[-1] = range(min(r_p[0], r[0]), max(r_p[-1] + 1, r[-1] + 1))
            else:
                xranges.append(r)

        fresh_ids = 0
        for xrange in xranges:
            fresh_ids += len(xrange)

        return fresh_ids
