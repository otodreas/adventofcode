import numpy as np


class FreshChecker:
    def __init__(self):
        pass

    def get_ranges(self, data):
        # Get indices of ranges and sort by starting index
        range_indices_array = np.zeros((len(data), 2), dtype=np.int64)
        for i, r in enumerate(data):
            nums = r.split("-")
            range_indices_array[i] = np.array([nums[0], int(nums[1]) + 1])

        range_indices_array_sorted = np.sort(range_indices_array, 0)

        # Create list of ranges based on indices
        ranges = []
        for r in range_indices_array_sorted:
            ranges.append(range(r[0], r[1]))

        self.ranges = ranges

    def check_fresh(self, id):
        for r in self.ranges:
            if id in r:
                return True
        return False

    def count_fresh_ids(self):
        # Compile list of exclusive ranges
        xranges = [self.ranges[0]]
        for r in self.ranges[1:]:
            r_p = xranges[-1]
            # Update exclusive range or create new if it doesn't overlap with previous ranges
            if (r_p[0] < r[-1] + 1 and r[0] < r_p[-1] + 1):
                xranges[-1] = range(min(r_p[0], r[0]), max(r_p[-1] + 1, r[-1] + 1))
            else:
                xranges.append(r)

        # Count the number of id's in xranges
        fresh_ids = 0
        for xrange in xranges:
            fresh_ids += len(xrange)

        return fresh_ids
