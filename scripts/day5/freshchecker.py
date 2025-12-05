import numpy as np


class FreshChecker:
    def __init__(self):
        pass

    def get_ranges(self, data):
        # Get indices of ranges and sort by starting index
        range_indices_array = np.zeros((len(data), 2), dtype=np.int64)
        for i, r in enumerate(data):
            nums = r.split("-")
            range_indices_array[i] = np.array([nums[0], nums[1]])
        range_indices_array_sorted = np.sort(range_indices_array, 0)
        self.ranges = range_indices_array_sorted

    def check_fresh(self, id):
        for r in self.ranges:
            if r[0] <= id <= r[1]:
                return True
        return False

    def count_fresh_ids(self):
        # Compile list of arrays containing exclusive ranges
        xranges = [[self.ranges[0][0], self.ranges[0][1]]]
        for r in self.ranges[1:]:
            r_p = xranges[-1]
            # Update exclusive range or create new if it doesn't overlap with previous ranges
            if r_p[0] <= r[1] and r[0] <= r_p[1]:
                xranges[-1] = [min(r_p[0], r[0]), max(r_p[1], r[1])]
            else:
                xranges.append(r)

        # Count the number of id's in xranges
        fresh_ids = 0
        for xrange in xranges:
            fresh_ids += len(range(xrange[0], xrange[1] + 1))
        return fresh_ids
